import json
import os

from featureExtraction import load_features

# This code saves the features of all the audios in separate JSON files depending on what partition they are from


pathLabels ='/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/labels_consensus.json'
audioPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio'


# Opening JSON file
with open(pathLabels) as json_file:
    data = json.load(json_file) # Python Dictionary with labels for each audio

# 4 new dictionaries for the train, test1, test2 and development
length = len(data)
trainDic = {}
testADic = {}
testBDic = {}
test2Dic = {}
devDic = {}
durations = {}

i = 0
# Para cada audio extraigo las features y las añado a su value del json (otro diccionario)
for audio in data.keys():
    # if 1000%(i+1)==0: 
    print(f"\n{i} de {length}\nDurations", durations)
    speakerActual = data[audio]['SpkrID']

    # print("\nAudio", audio)

    # Extract the features
    audioFile = os.path.join('/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio', audio ) # Gives the path to the os joining with a '/' both arguments
    featureDf, duration = load_features(audioFile)

    print("Duration", duration)

    # Extract the name of the features and their values
    featNames = list(featureDf.columns.values)
    values = map(float,list(featureDf.values[0]))

    # Create a new dictionary with pairs { Feature name : Feature value }
    dic = dict(zip(featNames,values))

    data[audio].update(dic)

    # Add this to new dictionary as the value for the new data dictionary
    if data[audio]['Split_Set'] == 'Test1':
        if speakerActual not in durations and speakerActual != 'Unknown':
            testADic[audio] = data[audio]
            durations[speakerActual] = [duration,duration]
        elif durations[speakerActual][0]< 200:
            testADic[audio] = data[audio]
            durations[speakerActual] = [durations[speakerActual][0]+ duration,durations[speakerActual][1] + duration]
        else:
            testBDic[audio] = data[audio]
            durations[speakerActual] = [durations[speakerActual][0],durations[speakerActual][1]+ duration]
    if data[audio]['Split_Set'] == 'Test2':
        test2Dic[audio] = data[audio]
    if data[audio]['Split_Set'] == 'Train':
        trainDic[audio] = data[audio]
    if data[audio]['Split_Set'] == 'Development':
        devDic[audio] = data[audio]
    i+=1

with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/train/train.json", "w") as outfile:
    json.dump(trainDic, outfile,indent=4)
    print("\nTrain Guardado !!! :)\n" )
with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/testA.json", "w") as outfile:
    json.dump(testADic, outfile,indent=4)
    print("\nTest A Guardado !!! :)\n" )
with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/testB.json", "w") as outfile:
    json.dump(testBDic, outfile,indent=4)
    print("\nTest B Guardado !!! :)\n" )
with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/test2.json", "w") as outfile:
    json.dump(test2Dic, outfile,indent=4)
    print("\nTest 2 Guardado !!! :)\n" )
with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/development/development.json", "w") as outfile:
    json.dump(devDic, outfile,indent=4)
    print("\nDevelopment Guardado !!! :)\n" )
with open("/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/test/testABdurations.json", "w") as outfile:
    json.dump(durations, outfile,indent=4)
    print("\nDurations Guardado !!! :)\n" )