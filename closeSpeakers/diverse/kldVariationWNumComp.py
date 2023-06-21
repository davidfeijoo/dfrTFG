import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from computeKLD import computeKLD
import matplotlib.pyplot as plt

# For every speaker in the speakerList, fit the GMMs of the different number of components from ncomponentsList
# The plot shows the lines of each speaker

testspeakerID = 17

pcaMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/newFeatures/newPcaMatrix58.txt'
trainSpeakersPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/trainSpeakersList.txt'

# Parameters
ncomponentsList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
speakerList = np.loadtxt(trainSpeakersPath)[0:10]

# Load the necessary for doing the projections

print("Loading cositas...")
trainData = pd.read_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/trainData.feather')
testData = pd.read_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestA.feather')
print("Loading pca matrix...")
pcaMatrix = np.loadtxt(pcaMatrixPath)
print("Pca matrix shape", pcaMatrix.shape)
print("Loading scaler...")
scaler = pickle.load(open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/scaler.pkl' ,mode = 'rb'))
print("Loaded!")

# Start computing KLD between the test speaker and all the train speakers
speakers = {}
dictKLDsNCOM = {}
for speaker in speakerList:
    KLDs = []
    variances = []
    for ncomponents in ncomponentsList:
        if speaker == speakerList[0]: dictKLDsNCOM[ncomponents] = {}
        KLD,variance = computeKLD(trainData,testData,testspeakerID,speaker,pcaMatrix,n_GMMs = 10,n_components = ncomponents,scaler=scaler)
        if not str(KLD).startswith('F'):
            KLDs.append(KLD)
            variances.append(variance)
            dictKLDsNCOM[ncomponents][speaker] = KLD
        else:
            KLDs.append(None)
            variances.append(None)
            dictKLDsNCOM[ncomponents][speaker] = None
            
    speakers[speaker] = (KLDs,variances)

for speaker in speakerList:
    lines = plt.plot(ncomponentsList,speakers[speaker][0],label = f"KLD speaker {int(speaker)} (- sentences)")
    color = lines[0].get_color()
    # plt.plot(ncomponentsList,speakers[speaker][1],label = f"Variances speaker {int(speaker)}", linestyle = "dotted",color = color)

for ncomp in dictKLDsNCOM.keys():
    sorted_KLDs = dict(sorted(dictKLDsNCOM[ncomp].items(), key=lambda item: item[1]))
    closeSpeakers = list(sorted_KLDs.keys())
    print(f"\n Sorted KLDs for ncomponents {ncomp}: {sorted_KLDs}")
    print(f"Close speakers for {ncomp} components: {closeSpeakers}\n")

plt.title(f'N components GMM - KLD to target speaker {testspeakerID}')
plt.xlabel('Number of components in the GMM')
plt.ylabel(f'KLD to speaker {testspeakerID}')
plt.legend()
plt.show()




