import pickle
import numpy as np
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler


globalFMPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/globalFM.txt'
speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeatures.pkl'

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nLoading global feature matrix and feature dict...:  {current_time}")

globalFM = np.loadtxt(globalFMPath)

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nLoaded!!!:  {current_time}\n")

# Normalise the features to save them in a dict:

# Scaling 1: de max y min totales: Extract the max and min values of all the speakers' features for normalisation
maxVal = globalFM.max()
minVal = globalFM.min()
print("Maximum Value in the global FM: ", maxVal)
print("Minimum Value in the global FM: ", minVal)


for speaker in dic.keys():
    if speaker == '2': print("Features speaker 2 antes de normalizar: ",dic[speaker])
    dic[speaker] = (dic[speaker]-minVal)/(maxVal-minVal)
    if speaker == '2': 
        print("Features speaker 2 después de normalizar: ",dic[speaker])
        print("Max feature speaker 2: ", np.max(dic[speaker]))
        print("Min feature speaker 2: ", np.min(dic[speaker]))



# Scaling 2: de max y min de cada feature
# mmscaler = MinMaxScaler()
# normalisedData = mmscaler.fit(globalFM)
# print("Maximum values from the global FM: ", mmscaler.data_max_)
# print("Minimum values from the global FM: ", mmscaler.data_min_)

# for speaker in dic.keys():
#     if speaker == '2': print("Features speaker 2 antes de normalizar: ",dic[speaker])
#     dic[speaker] = mmscaler.transform(dic[speaker])
#     if speaker == '2': 
#         print("Features speaker 2 después de normalizar: ",dic[speaker])
#         print("Max feature speaker 2: ", np.max(dic[speaker]))
#         print("Min feature speaker 2: ", np.min(dic[speaker]))

# Mean substraction: Substracting the mean vector to all the vectors
# f = meanFeatureVector(globalFM) #f is the mean feature vector.
# M = 0
# for speaker in dic: 
#     i = 0
#     for sentence in dic[speaker]:
#         dic[speaker][i] = sentence - f
#         i+=1
#         M+=1
# print("Total utterances number (M): ", M)


# Saving normalised dictionary
now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"Saving normalised dictionary:  {current_time}")

with open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesMinMaxGlobal.pkl',mode = 'wb') as pkl_speakerFile:
    pickle.dump(dic,pkl_speakerFile)

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"Saved normalised dictionary !!!!!!!!!:  {current_time}")