import pandas as pd
from datetime import datetime

trainingDataPath = "/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/trainData.feather"
testAdataPath = "/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestA.feather"
savePath = "/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/trainAndNewTestA.feather"


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoading train...:  {current_time}\n")

dftrain = pd.read_feather(trainingDataPath)
print(dftrain)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoaded train! Loading test A...:  {current_time}\n")

dftest = pd.read_feather(testAdataPath)
print(dftest)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoaded test! Joining train and test A...:  {current_time}\n")

newDf = pd.concat([dftrain,dftest], ignore_index=True)
print(newDf)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nSaving new dataframe...:  {current_time}\n")

newDf.to_feather(savePath)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nSaved!:  {current_time}\n")