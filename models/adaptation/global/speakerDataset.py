import pandas as pd
import numpy as np
from datetime import datetime

from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import torch

from sklearn.preprocessing import StandardScaler


class myDataset(Dataset):
    def __init__(self, features_and_labels_file,name,scaler = None):

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"\n\nLoading {name} dataset...:  {current_time}\n")

        self.data = pd.read_feather(features_and_labels_file)

        # Save the names of the audios and labels and features
        self.audios = self.data.get('Audio') # Names of the audios
        self.features = self.data.iloc[:,8:]
        self.labels = self.data.iloc[:,2:5]
        
        # Standarisation 
        if scaler is None:
            self.scaler = StandardScaler()
            self.features = self.scaler.fit_transform(self.features)
        else:
            self.scaler = scaler
            self.features = self.scaler.transform(self.features)
            # print("Scaled features\n",self.features)
        
        self.mean = self.scaler.mean_
        self.std = self.scaler.var_

        print("\nData:\n ",self.data)
        print(f"\nNumber of samples in {name} dataset {len(self.data)}\n")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Finished loading {name} dataset:  {current_time}")


    def __len__(self):
        return len(self.data)
        

    def __getitem__(self, idx):
        
        audio = self.data.iloc[idx,0]

        arousal = float(str(self.data.loc[idx,'EmoAct'])) # Arousal label
        dominance = float(str(self.data.loc[idx,'EmoDom'])) # Dominance label
        valence = float(str(self.data.loc[idx,'EmoVal'])) # Valence label
        label = [arousal,dominance,valence]
        
        features = np.array(self.features[idx,:]) # All the 6373 features values
        features = np.array(list(map(float,features))) # Convert the strings to float
        features = np.clip(features, - 3 , + 3 ) # Mean is 0 and std is 1 for all the features
        
        return features, label

    
def test():

    test_data = myDataset(
        "/Users/davidfeijoo/bussoImplementation/MSP_podcast/pruebas/testAData.feather","test A"
    )
    
    # Testing
    print(f"\nData type {type(test_data.data)}")
    print(f"\nMean : {test_data.scaler.mean_}")
    print(f"\nSTD 3874: {test_data.scaler.var_}\n")
    print("\nAudios\n",test_data.audios)
    print("\nLabels\n",test_data.labels)
    print("\nValence\n",test_data.data.get('EmoVal'))
    print("\nFeatures\n",test_data.features)
    print("\nMax feature of each \n", test_data.features.max(axis = 0))
    print("\nMin feature of each \n", test_data.features.min(axis = 0))
    print("\nGlobal max feature \n", max(test_data.features.max(axis = 0)))
    print("\nGlobal min feature \n", min(test_data.features.min(axis = 0)))
    print("\nMean from each feature\n",test_data.features.mean(axis = 0))
    print("\nMax mean: ", max(test_data.features.mean(axis = 0)))
    print("\nMin mean: ", min(test_data.features.mean(axis = 0)))
    print("\nStd from each feature\n",test_data.features.std(axis = 0))
    print("\nMax std: ", max(test_data.features.std(axis = 0)))
    print("\nMin std: ", min(test_data.features.std(axis = 0)))
    print("\nFeatures 3874\n",test_data.features[:,3874])
    print("\nMax Feature 3874\n",max(test_data.features[:,3874]))
    print("\nMin Feature 3874\n",min(test_data.features[:,3874]))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    test_dataloader = DataLoader(test_data, batch_size=16, shuffle=False)
    for i , (labels, inputs) in enumerate(test_dataloader):
        if i == 0:
            print(labels)
            print(inputs)
            labels = labels[2]
            print(labels)
            inputs, labels = inputs.to(device), labels.to(device)
    print("Mean", test_data.mean)
    print("STD",test_data.std)

    # for i, (inputs, labels) in enumerate(test_dataloader):
    #     print(inputs)
    #     print("Features shape: ",np.shape(inputs))
    #     # print(labels)

    # test_data.afternorm()