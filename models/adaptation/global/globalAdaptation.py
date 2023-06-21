import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

import pickle

from nnAdap import NeuralNetwork
from speakerDataset import myDataset

def adaptation(modelName, attribute, batch_size=32, plain = 'plain', approach = 'Unique' , pc = 0, random_seed = 0, gadi = None):

    num_epochs=100
    learning_rate=0.0001

    # Attribute choice
    if attribute == 'arousal':
        idx = 0
        dropout_rate = 0.5
        if gadi: modelPath = f"/scratch/wa66/dr2845/models/trainedModels/baseline/arousal/arousal_1_0.001_512.pth" 
        else: modelPath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/baseline/arousal/arousal_1_0.001_512.pth"

    elif attribute == 'dominance':
        idx = 1
        dropout_rate = 0.5
        if gadi: modelPath = f"/scratch/wa66/dr2845/models/trainedModels/baseline/dominance/dominance_1_0.001_512.pth" 
        else: modelPath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/baseline/dominance/dominance_1_0.001_512.pth"

    else:
        idx = 2  # Valence
        dropout_rate = 0.7
        if gadi: modelPath = f"/scratch/wa66/dr2845/models/trainedModels/baseline/valence/valence_1_0.001_32.pth"  # Model and optimizer weights paths
        else: modelPath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/baseline/valence/valence_1_0.001_32.pth"


    print("\nGadi:", gadi)
    print("Model name:", modelName)
    print(f"Attribute: {attribute}. Dropout rate: {dropout_rate}. Batch Size: {batch_size} ")
    print("Learning rate:", learning_rate)
    print(f"Evaluation on: {plain} test B\nApproach: {approach}")
    
    # Load the database/{plain}s
    if gadi:
        # Load the scaler 
        scaler = pickle.load(open(f'/scratch/wa66/dr2845/models/database/scaler.pkl' ,mode = 'rb'))

        # Save path
        savePath = f"/scratch/wa66/dr2845/models/trainedModels/adaptation/global/{plain}/{approach}/{attribute}/bestDevLoss/{modelName}_{learning_rate}_{batch_size}.pth"
        saveAdapPath = f"/scratch/wa66/dr2845/models/trainedModels/adaptation/global/{plain}/{approach}/{attribute}/bestAdapLoss/{modelName}_{learning_rate}_{batch_size}.pth"

        # Load the datasets in GADI
        adaptation_data = myDataset(f"/scratch/wa66/dr2845/models/database/{plain}/{pc}pc/adaptation{approach}Data.feather", "adaptation",scaler=scaler)
        adaptation_loader = DataLoader(adaptation_data, batch_size = batch_size, shuffle=True)
        development_data = myDataset(f"/scratch/wa66/dr2845/models/database/developmentData.feather", "development", scaler = scaler)
        development_loader = DataLoader(development_data, batch_size = len(development_data), shuffle=False)
        test_data = myDataset(f"/scratch/wa66/dr2845/models/database/{plain}/{plain}TestB.feather",f"{plain}TestB",scaler = scaler)
        test_loader = DataLoader(test_data, batch_size = len(test_data), shuffle = False)
    else:
        # Load the scaler 
        scaler = pickle.load(open(f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/scaler.pkl' ,mode = 'rb'))

        # Save path
        savePath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/adaptation/global/{plain}/{approach}/{attribute}/bestDevLoss/{modelName}_{learning_rate}_{batch_size}.pth"
        saveAdapPath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/adaptation/global/{plain}/{approach}/{attribute}/bestAdapLoss/{modelName}_{learning_rate}_{batch_size}.pth"
        
        # Load the datasets locally
        adaptation_data = myDataset(f"/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{plain}/{pc}pc/adaptation{approach}Data.feather", "adaptation",scaler=scaler)
        adaptation_loader = DataLoader(adaptation_data, batch_size, shuffle=True)
        development_data = myDataset(f"/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/developmentData.feather", "development", scaler = scaler)
        development_loader = DataLoader(development_data, batch_size = len(development_data), shuffle=True,drop_last = True)
        test_data = myDataset(f"/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{plain}/{plain}TestB.feather",f"{plain}TestB",scaler = scaler)
        test_loader = DataLoader(test_data, batch_size = len(test_data), shuffle = True,drop_last = True) #drop_last = True

    print("\nLoaded model:", modelPath.split('/')[-1])

    patience=15

    # Create the neural network
    model = NeuralNetwork(dropout_rate).double() # inputs are float64 and model is float32, use this line to convert the model to float64

    # Move the model to the GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    print("Running on device:", device,"\n")

    # Load the model and optimizer state_dicts
    checkpoint = torch.load(modelPath,map_location=device)

    # Apply pretrained model weights
    model.load_state_dict(checkpoint['model_state_dict'])

    # Freeze the weights of the first layers
    for param in model.parameters():
        param.requires_grad = False

    # Enable weight updates in the last layer
    for param in model.output_layer.parameters():
        param.requires_grad = True

    # Define the optimizer
    # optimizer = optim.SGD(filter(lambda p: p.requires_grad, model.parameters()), learning_rate, momentum=0.9,)
    optimizer = optim.SGD(model.parameters(), learning_rate, momentum=0.9)
    optimizer.load_state_dict(checkpoint['optimizer_state_dict']) 

    # You must call model.eval() to set dropout and batch normalization layers to evaluation mode before running inference. 
    # Failing to do this will yield inconsistent inference results. (pytorch)
    model.eval()
    torch.manual_seed(random_seed)

    test_loss = 0.0
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(test_loader):
            labels = labels[idx]
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = ccc_loss(labels, outputs)
            test_loss += loss.item()
        test_loss /= len(test_loader)
    print(f"Test loss: {test_loss:.4f}\n")
    initial_loss = test_loss

    # Training loop
    losses = {}
    losses["adap"] = []
    losses["val"] = []
    losses["test"] = []
    best_dev_loss = float('inf')
    best_adap_loss = float('inf')
    epochs_not_improving = 0

    for epoch in range(num_epochs):
        model.train()
        adap_loss = 0.0

        print("\nEpoch:", epoch + 1)

        for i, (inputs, labels) in enumerate(adaptation_loader):
            labels = labels[idx]
            inputs, labels = inputs.to(device), labels.to(device) 
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = ccc_loss(labels, outputs)
            loss.backward()
            optimizer.step()

            adap_loss += loss.item()

        adap_loss /= len(adaptation_loader)
        print(f"Training: Epoch {epoch + 1} finished")

        # Validation
        model.eval()
        dev_loss = 0.0
        with torch.no_grad():
            for i, (inputs, labels) in enumerate(development_loader):
                labels = labels[idx]
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                loss = ccc_loss(labels, outputs)
                dev_loss += loss.item()

            dev_loss /= len(development_loader)
            print(f"Validating: Epoch {epoch + 1} finished")

        test_loss = 0.0
        with torch.no_grad(): #Monitoring test loss
            for i, (inputs, labels) in enumerate(test_loader):
                labels = labels[idx]
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                loss = ccc_loss(labels, outputs)
                test_loss += loss.item()
            test_loss /= len(test_loader)
        print(f"Testing: Epoch {epoch + 1} finished")

        # Print training and evaluation loss
        print(f"Epoch {epoch + 1}/{num_epochs}, train loss: {adap_loss:.4f}, val loss: {dev_loss:.4f}, test loss: {test_loss:.4f}")
        losses['adap'].append(adap_loss)
        losses['val'].append(dev_loss)
        losses['test'].append(test_loss)
         

        # Saving best model on the adaptation set
        if adap_loss < best_adap_loss: 
            best_adap_loss = adap_loss
            best_model = model.state_dict()
            torch.save({'model_state_dict': best_model, 'adap_loss': adap_loss, 'dev_loss': dev_loss, 'test_loss' : test_loss}, saveAdapPath)
            print("Best adaptation loss until now")

        # Early stopping
        if dev_loss < best_dev_loss:
            best_dev_loss = dev_loss
            epochs_not_improving = 0
            best_model = model.state_dict()
            torch.save({'model_state_dict': best_model,'adap_loss': adap_loss,  'dev_loss': dev_loss, 'test_loss' : test_loss}, savePath)
            print("Model saved because it is the best until now!")
        else:
            epochs_not_improving += 1

        if epochs_not_improving >= patience:
            print(f"Early stopping triggered. No improvement in the last {patience} epochs.")
            if not gadi:
                for key in losses.keys():
                    plt.plot(range(epoch+1),losses[key], label = f'{key}')
                plt.legend()
                plt.show()
            break

        print("Epochs not improving:", epochs_not_improving)

    # Print the initial loss
    print(f"\n\nBaseline model loss: {initial_loss:.4f}")

    # Evaluate on the test set: best dev loss
    checkpoint = torch.load(savePath ,map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    test_loss = 0.0
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(test_loader):
            labels = labels[idx]
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = ccc_loss(labels, outputs)
            test_loss += loss.item()
        test_loss /= len(test_loader)
    print(f"Best development test loss: {test_loss:.4f}")

    # Evaluate on the test set: best adap loss
    checkpoint = torch.load(saveAdapPath ,map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    test_loss = 0.0
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(test_loader):
            labels = labels[idx]
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = ccc_loss(labels, outputs)
            test_loss += loss.item()
        test_loss /= len(test_loader)
    print(f"Best adaptation test loss: {test_loss:.4f}\n")


#  Loss function
def ccc_loss(x, y):

    y = y.squeeze()

    std_x = torch.std(x)
    std_y = torch.std(y)
    mean_x = torch.mean(x)
    mean_y = torch.mean(y)

    cov = torch.mean((x - mean_x) * (y - mean_y))

    loss = 1 - 2 * cov / (std_x**2 + std_y**2 + (mean_x - mean_y)**2)
    return loss
