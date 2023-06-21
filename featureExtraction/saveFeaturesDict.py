
import csv
import os
import json
import numpy as np
import pandas as pd 
import pickle


#Save a matrix of features for each speaker to use in the comparison of speakers

def saveFeatures(): # Guardar las features de cada sentence de usuario

    print("\nLoading training data...\n")
    with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/train/train.json", 'r') as trainf:
        trainData = json.load(trainf)
    print("\nTraining data loaded!\n")
    print("\nLoading test data...\n")
    with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/testA.json", 'r') as testAf:
        testAData = json.load(testAf)
    print("\nTest A data loaded!\n")

    sizeTrain = len(list(trainData.keys()))
    print("Number of train speakers" , sizeTrain)

    row_counter = 0
    speakerID = 0
    speakerDICTIONARY = {}
    featureArray = np.empty((0,6373))


    with open ('/Users/davidfeijoo/bussoImplementation/MSP_podcast/Speaker_ids_ordenado.txt') as csv_IDsFile:      
        csv_reader = csv.reader(csv_IDsFile, delimiter=';')


        for row in csv_reader:

            row_counter += 1
            audio = row[0]
            speakerID = row[1]
            # print("Row: " + str(row_counter))

            if (audio in trainData or audio in testAData) and trainData[audio]['SpkrID'] != 'Unknown': 

                print(f"\nAudio {audio} from speaker {speakerID}\n")
                if audio in trainData:
                    featureArray = pd.DataFrame(trainData[audio].values())[7:]
                elif audio in testAData:
                    featureArray = pd.DataFrame(testAData[audio].values())[7:]

                if speakerID not in speakerDICTIONARY:
                    # print(speakerDICTIONARY)
                    speakerDICTIONARY[speakerID] = np.row_stack((np.empty((0,6373)), featureArray.T))
                else:
                    speakerDICTIONARY[speakerID] = np.row_stack((speakerDICTIONARY[speakerID], featureArray.T))
    
    with open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakersFeatures.pkl',mode = 'wb') as pkl_speakerFile:
        pickle.dump(speakerDICTIONARY,pkl_speakerFile)
    print("Final speaker ID: " + str(speakerID))
    print("Number of train speakers" , sizeTrain)

    return
