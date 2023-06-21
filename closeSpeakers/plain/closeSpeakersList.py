import argparse
import pickle
import numpy as np

from computeKLD import computeKLD

parser = argparse.ArgumentParser()
parser.add_argument('--testSpeaker', type=int, required=True)
parser.add_argument('--gadi', default=False, action='store_true')
parser.add_argument('--pc' , type= int, choices= [35,58],required = True)
args = parser.parse_args()

testSpeaker = args.testSpeaker
gadi = args.gadi
pc = args.pc

# Choose which pca matrix
if pc == 35:
    com = 10
elif pc == 58:
    com = 77
else:
    raise Exception(f'There is no {pc} pca matrix, try 35 or 58')

if gadi:
    speakerFilePath = '/home/561/dr2845/closeSpeakers/closeSpeakersFeaturesStandardScaler.pkl'
    pcaMatrixPath = f'/home/561/dr2845/closeSpeakers/Intento 2/pcaMatrix{com}.txt'
    saveListPath = f'/home/561/dr2845/closeSpeakers/Intento 2/KLDs/KLDs_{pc}pc/closestSpeakers_testSpeaker_'+str(testSpeaker)+'.txt'
    trainSpeakersPath = '/home/561/dr2845/closeSpeakers/trainSpeakersList.txt'
else:
    speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesStandardScaler.pkl'
    pcaMatrixPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/pcaMatrix{com}.txt'
    saveListPath = f'/Users/davidfeijoo/bussoImplementation/Close speakers selection/Intento 2/KLDs/KLDs_{pc}pc/closestSpeakers_testSpeaker_'+str(testSpeaker)+'.txt'
    trainSpeakersPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/trainSpeakersList.txt'

# Load the necessary for doing the projections

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

pcaMatrix = np.loadtxt(pcaMatrixPath)

trainSpeakers = np.loadtxt(trainSpeakersPath)

# Start computing KLD between the test speaker and all the train speakers

KLDs = {}
variances = {}
for trainSpeaker in trainSpeakers:
    trainSpeaker = int(trainSpeaker)
    KLD,variance = computeKLD(dic,testSpeaker,trainSpeaker,pcaMatrix,n_GMMs=500,n_components=10)
    if not str(KLD).startswith('F'): ###CAMBIARLO !!!!!!!!!!
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

# Save the sorted list

np.savetxt(saveListPath,closeSpeakers)


