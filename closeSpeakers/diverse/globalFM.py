import numpy as np
import pandas as pd
from datetime import datetime


# # Load the dataframes
# print("\nLoading test and train...")
# testA = pd.read_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestA.feather')
# train = pd.read_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/trainData.feather')
# print("\nLoaded!\n")

# globalFM = np.empty((0,6373))

# # Get only the features from each dataframe
# featuresTest = testA.iloc[:,8:].to_numpy()
# print("Test shape", featuresTest.shape)
# featuresTrain = train.loc[train['SpkrID'] != 'Unknown'].iloc[:,8:].to_numpy()
# print("Train shape",featuresTrain.shape)

# print("\nCreating globalFM")
# globalFM = np.row_stack([featuresTest,featuresTrain])

# print("Saving globalFM")
# np.savetxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/newFeatures/newGlobalFM.txt',globalFM,fmt = '%s')

# # Load to check
# print("Loading matrix...")
# matrix = np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/newFeatures/newGlobalFM.txt')
# print("Loaded! Getting the shape...")
# print(matrix.shape)