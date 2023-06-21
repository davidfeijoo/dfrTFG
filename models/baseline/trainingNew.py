import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import pickle
from nn import NeuralNetwork
from speakerDatasetNew import myDataset
from datetime import datetime

def training(modelName,attribute,learning_rate = 0.001,batch_size = 32,dropout_rate = 0.7,gadi = False): 

    # Hyperparameters
    num_epochs = 200
    epochsNotImproving = 0
    shuffle = True

    print("\nGadi: ", gadi)
    print("Model Name: ", modelName)
    print("Learning rate: ", learning_rate)
    print("Batch Size: ",batch_size)
    print("Shuffle: ", shuffle)

    # Create the neural network
    model = NeuralNetwork(dropout_rate).double()

    print("Model type: ",model.layer1.weight.dtype)

    # Define the optimizer
    # optimizer = optim.Adam(model.parameters(), learning_rate)
    optimizer = optim.SGD(model.parameters(), learning_rate, momentum=0.9)
    
    if gadi:
        savePath = f"/scratch/wa66/dr2845/models/trainedModels/dependent/{attribute}/Speaker dependent Test A random/{modelName}_{learning_rate}_{batch_size}.pth"
        lossesPath = f"/scratch/wa66/dr2845/models/trainedModels/dependent/{attribute}/Extras Speaker dependent Test A random/{modelName}_{learning_rate}_{batch_size}_losses.pkl"

        # Load the scaler
        scaler = pickle.load(open('/scratch/wa66/dr2845/models/database/scaler.pkl' ,mode = 'rb'))

        # Load the datasets
        training_data = myDataset("/scratch/wa66/dr2845/models/database/trainData.feather","train",scaler)
        train_loader = DataLoader(training_data, batch_size, shuffle=shuffle,drop_last=True)
        # train_and_testA_data = myDataset("/scratch/wa66/dr2845/models/database/trainAndNewTestA.feather","trainAndNewTestA",scaler)
        # train_and_testA_loader = DataLoader(train_and_testA_data, batch_size= batch_size, shuffle=shuffle,drop_last=True)
        develop_data  = myDataset("/scratch/wa66/dr2845/models/database/developmentData.feather", "development",scaler)
        develop_loader = DataLoader(develop_data, batch_size = len(develop_data), shuffle=shuffle,drop_last=True)
        test_data = myDataset("/scratch/wa66/dr2845/models/database/testBData.feather","plainTestB",scaler)
        test_loader = DataLoader(test_data, batch_size= len(test_data), shuffle=shuffle,drop_last=True)
        test_data2 = myDataset("/scratch/wa66/dr2845/models/database/newTestB.feather"," diverseTestB",scaler)
        test_loader2 = DataLoader(test_data2, batch_size= len(test_data2),  shuffle=shuffle,drop_last=True)


    else:
        savePath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/baseline/{attribute}/{modelName}_{learning_rate}_{batch_size}.pth"
        lossesPath = f"/Users/davidfeijoo/bussoImplementation/models/trainedModelsLocal/baseline/{attribute}/{modelName}_{learning_rate}_{batch_size}_losses.pkl"

        # Load the scaler
        scaler = pickle.load(open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/scaler.pkl' ,mode = 'rb'))

        # Load the datasets local
        training_data = myDataset("/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/trainData.feather","train",scaler)
        train_loader = DataLoader(training_data, batch_size, shuffle=shuffle,drop_last=True) 
        # train_and_testA_data = myDataset("/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/trainAndNewTestA.feather","trainAndNewTestA",scaler)
        # train_and_testA_loader = DataLoader(train_and_testA_data, batch_size= batch_size, shuffle=shuffle,drop_last=True)
        develop_data  = myDataset("/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/developmentData.feather", "development",scaler)
        develop_loader = DataLoader(develop_data, batch_size= len(develop_data), shuffle=shuffle,drop_last=True)
        test_data = myDataset("/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/testBdata.feather"," plainTestB",scaler)
        test_loader = DataLoader(test_data, batch_size= len(test_data),  shuffle=shuffle,drop_last=True)
        test_data2 = myDataset("/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestB.feather"," diverseTestB",scaler)
        test_loader2 = DataLoader(test_data2, batch_size= len(test_data2),  shuffle=shuffle,drop_last=True)

    if attribute == 'arousal':
        idx = 0
    elif attribute == 'dominance':
        idx = 1
    else:
        idx = 2 # Valence
    
    print("Attribute: ", attribute , ", Idx: ", idx, "\n")
    
    # Move the model to the GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    print("Running in device: ",device)

    # Training loop
    best_val_loss = float('inf')
    best_model = None
    losses = {}
    losses["train"] = []
    losses["val"] = []

    patience = 30

    for epoch in range(num_epochs):
        
        model.train()
        train_loss = 0.0

        print("\nEpoch: ",epoch +1 )

        for i, (inputs, labels) in enumerate(train_loader): 
            labels = labels[idx] # Gets the labels for arousal, dominance or valence only
            inputs, labels = inputs.to(device), labels.to(device)

            if i%100 == 0: print("Training: ",i)

            # Zero the parameter gradients
            optimizer.zero_grad()
            outputs = model(inputs) # forward 
            loss = ccc_loss(labels, outputs) 
            # print(f"Loss {i}",loss.item())
            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        train_loss /= len(train_loader)
        print(f"Training: {epoch+1} finished")

        # Validation
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for i, (inputs, labels) in enumerate(develop_loader):
                labels = labels[idx]
                if i%100 == 0: print("Validating: ", i)
                inputs, labels = inputs.to(device), labels.to(device)
                outputs = model(inputs)
                loss = ccc_loss(labels, outputs)
                val_loss += loss.item()

            val_loss /= len(develop_loader)
            print(f"Validating: {epoch+1} finished")


        # Print training and evaluation loss
        print(f"Epoch {epoch+1}/{200}, train loss: {train_loss:.4f}, val loss: {val_loss:.4f}")
        losses['train'].append(train_loss)
        losses['val'].append(val_loss)
         
        # Check for early stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochsNotImproving = 0
            best_model = model.state_dict()
            best_optimizer = optimizer.state_dict()
            torch.save({'model_state_dict': best_model, 'optimizer_state_dict' : best_optimizer, 'train_loss': train_loss, 'val_loss' : val_loss}, savePath)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(f"\nModel saved because it is the best until now!: {current_time}\n")
        else:
            epochsNotImproving +=1 
            if epochsNotImproving >= patience:
                pickle.dump(losses,open(lossesPath,mode = 'wb'))
                print(f"Early stopping triggered. No improvement in the last {patience} epochs.")
                break
        
        print("Epochs not improving: ",epochsNotImproving)

    # Evaluate on the test set
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
    print(f"\nTest loss plain: {test_loss:.4f} , CCC = {(1-test_loss):.4f}")

    test_loss2 = 0.0
    with torch.no_grad():
        for i, (inputs, labels) in enumerate(test_loader2):
            labels = labels[idx]
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = ccc_loss(labels, outputs)
            test_loss2 += loss.item()
        test_loss2 /= len(test_loader2)
    print(f"\nTest loss diverse: {test_loss2:.4f} , CCC = {(1-test_loss2):.4f}")

# Loss function
def ccc_loss(x, y):

    y = y.squeeze()
    
    std_x = torch.std(x)
    std_y = torch.std(y)
    mean_x = torch.mean(x)
    mean_y = torch.mean(y)

    # print((x - mean_x) * (y - mean_y))
    cov = torch.mean((x - mean_x) * (y - mean_y))

    loss = 1 - 2 * cov / (std_x**2 + std_y**2 + (mean_x - mean_y)**2)
    return loss

    
