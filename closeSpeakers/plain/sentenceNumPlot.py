import argparse
import pickle
import numpy as np
import matplotlib.pyplot as plt

from computeKLD import computeKLD


testSpeaker = 15


speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesStandardScaler.pkl'
pcaMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/pcaMatrix.txt'
trainSpeakersPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/trainSpeakersList.txt'

# Load the necessary for doing the projections

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

pcaMatrix = np.loadtxt(pcaMatrixPath)

trainSpeakers = np.loadtxt(trainSpeakersPath)[0:30]

# Start computing KLD between the test speaker and all the train speakers

KLDs = {}
variances = {}
for trainSpeaker in trainSpeakers:
    trainSpeaker = int(trainSpeaker)
    KLD,variance = computeKLD(dic,testSpeaker,trainSpeaker,pcaMatrix,n_GMMs=100,n_components=25)
    if not str(KLD).startswith('F'):
        KLDs[trainSpeaker] = KLD
        variances[trainSpeaker] = variance


# We sort the train speakers in an increasing order of KLD 

sorted_KLDs = dict(sorted(KLDs.items(), key=lambda item: item[1]))
closeSpeakers = list(sorted_KLDs.keys())
print(f"\nSorted KLDs:\n")
print(sorted_KLDs)
print(f"\nClosest speakers to speaker {testSpeaker}:\n")
print(closeSpeakers,"\n")
print(f"\nVariances {testSpeaker}:\n")
print(variances,"\n")


n_sentences = []
for speaker in closeSpeakers:
    n_sentences.append(dic[str(int(speaker))].shape[0])
plt.plot(list(range(len(closeSpeakers))), n_sentences )

plt.title('Ordered speakers')
plt.xlabel('Sorted closest speakers')
plt.ylabel(f'Number of samples')
plt.show()
