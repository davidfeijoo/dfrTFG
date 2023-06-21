from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self, dropout_rate):
        super(NeuralNetwork, self).__init__()
        
        # Layers
        self.layer1 = nn.Linear(6373, 512)
        self.bn1 = nn.BatchNorm1d(512)
        self.dropout1 = nn.Dropout(p=dropout_rate)
        self.layer2 = nn.Linear(512, 512)
        self.bn2 = nn.BatchNorm1d(512)
        self.dropout2 = nn.Dropout(p=dropout_rate)
        self.layer3 = nn.Linear(512, 512)
        self.bn3 = nn.BatchNorm1d(512)
        self.dropout3 = nn.Dropout(p=dropout_rate)
        self.layer4 = nn.Linear(512, 512)
        self.bn4 = nn.BatchNorm1d(512)
        self.dropout4 = nn.Dropout(p=dropout_rate)
        self.output_layer = nn.Linear(512, 1)
        
        # Activation function
        self.relu = nn.ReLU()
        
    def forward(self, x):
        # Pass the input through the layers and activation functions
        x = self.dropout1(self.bn1(self.relu(self.layer1(x))))
        x = self.dropout2(self.bn2(self.relu(self.layer2(x))))
        x = self.dropout3(self.bn3(self.relu(self.layer3(x))))
        x = self.dropout4(self.bn4(self.relu(self.layer4(x))))
        x = self.output_layer(x)
        
        return x

