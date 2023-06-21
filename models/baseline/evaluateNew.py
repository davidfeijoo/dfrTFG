import torch
from torch.utils.data import DataLoader

import pickle

from speakerDatasetNew import myDataset
from nn import NeuralNetwork

def evaluate(path,attribute,model_name,batch_size,gadi):

    print('\n')
    # print("Batch Size: ",batch_size)
    print("Model Name: ", model_name)
    print("Gadi: ", gadi)


    if attribute == 'arousal':
        idx = 0
        dropout_rate = 0.5
    elif attribute == 'dominance':
        idx = 1
        dropout_rate = 0.5
    else:
        idx = 2 # Valence
        dropout_rate = 0.7

    
    print("Attribute: ", attribute , ", Idx: ", idx,"\n")

    model = NeuralNetwork(dropout_rate).double()
    
    # Move the model to the GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Load the model and optimizer state_dicts
    checkpoint = torch.load(path,map_location=device)

    # Apply pretrained model weights
    model.load_state_dict(checkpoint['model_state_dict'])

    if gadi:
        # For testing in GADI
        scaler = pickle.load(open('/scratch/wa66/dr2845/models/database/scaler.pkl' ,mode = 'rb'))
        test_data = myDataset("/scratch/wa66/dr2845/models/database/testBData.feather","test B",scaler)
        test_loader = DataLoader(test_data, batch_size = len(test_data), shuffle = False)
    else:
        scaler = pickle.load(open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/scaler.pkl' ,mode = 'rb'))
        test_data = myDataset("/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestB.feather","newTestB",scaler)
        test_loader = DataLoader(test_data, batch_size=len(test_data), shuffle = False)
    
    # Evaluate on the test set
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
    print(f"\nTest loss: {test_loss:.4f}\n")
    return

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
