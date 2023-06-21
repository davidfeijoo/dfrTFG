from joinFeatures1000 import joinFeatures
import json
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

datasetPaths = ['/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/testA.json',
                '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/testB.json',
                '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/train/train.json',
                '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/development/development.json']


for path in datasetPaths:

    splittedPath = path.split("/")
    dataset = splittedPath[-1].split(".")[0]
    savePath = f'/scratch/wa66/dr2845/{dataset}Data.feather'

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nSaved data feather correctly!:  {current_time}\n")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nLoading data from {dataset}.json...:  {current_time}\n")

    # Load the data from the file
    with open(path, 'r') as f:
        dict = json.load(f)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\n{dataset} dataset loaded! Ready to start the process:  {current_time}\n")


    # Json to data

    dics = list(dict.values())
    audios = list(dict.keys())
    data = joinFeatures(dics,audios)

    labels = data[:,2:5]
    features = data[:,8:]
    print("Audios", data[:,0])
    print("Labels", labels)
    print("features", features)
    
    # Save the data in a file for later use: ############################################################################################################################

    # Feather ######################################################

    # Convert to pd.DataFrame first

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nTo dataframe...:  {current_time}\n")
    columnNames = []
    columnNames.append('Audio')
    columnNames.extend(dics[0].keys())
    df = pd.DataFrame(data)
    df.columns = columnNames
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nDataframe done...:  {current_time}\n")

    print(df)

    # Save

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nSaving data feather...:  {current_time}\n")

    df.to_feather(savePath)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nSaved data feather!:  {current_time}\n")

    # Load

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nLoading data feather...:  {current_time}\n")

    df = pd.read_feather(savePath)
    print(df)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"\nLoaded data feather!:  {current_time}\n")

    # Numpy ######################################################## 

    # Save

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nSaving data np...:  {current_time}\n")

    # np.save(f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/pruebas/{dataset}Data.npy',data)

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nSaved np!:  {current_time}\n")

    # # Load

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nLoading data np...:  {current_time}\n")

    # npLoaded = np.load(f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/pruebas/{dataset}Data.npy')

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nLoaded np!:  {current_time}\n")


    # Pickle ########################################################

    # Save

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nSaving data pickle...:  {current_time}\n")

    # with open(f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/pruebas/{dataset}Data.pkl',mode = 'wb') as pkl_speakerFile:
    #     pickle.dump(data,pkl_speakerFile)

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nSaved pickle!:  {current_time}\n")

    # Load

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nLoading data pickle...:  {current_time}\n")

    # with open(f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/pruebas/{dataset}Data.pkl',mode = 'rb') as pkl_speakerFile:
    #     pklLoaded = pickle.load(pkl_speakerFile)

    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(f"\nLoaded pickle!:  {current_time}\n")

    ###################################################################