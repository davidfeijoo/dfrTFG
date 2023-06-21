import argparse
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

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
    trainPath = '/scratch/wa66/dr2845/models/database/trainData.feather'
    testPath = '/scratch/wa66/dr2845/models/database/diverse/diverseTestA.feather'
    pcaMatrixPath = f'/home/561/dr2845/closeSpeakers/Intento 3/newPcaMatrix{com}.txt'
    saveListPath = f'/home/561/dr2845/closeSpeakers/Intento 3/KLDs/KLDs_{pc}pc/closestSpeakers_testSpeaker_'+str(testSpeaker)+'.txt'
    trainSpeakersPath = '/home/561/dr2845/closeSpeakers/trainSpeakersList.txt'
else:
    trainPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/trainData.feather'
    testPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/diverseTestA.feather'
    pcaMatrixPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/newFeatures/newPcaMatrix{com}.txt'
    saveListPath = f'/Users/davidfeijoo/bussoImplementation/Close speakers selection/Intento 3/KLDs/KLDs_{pc}pc/closestSpeakers_testSpeaker_'+str(testSpeaker)+'.txt'
    trainSpeakersPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/trainSpeakersList.txt'
    scalerPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/scaler.pkl'

# Load the necessary for doing the projections


print("Loading cositas...")
trainData = pd.read_feather(trainPath)
testData = pd.read_feather(testPath)
print(f"Loading pca matrix {com} components, {pc}% variance...")
pcaMatrix = np.loadtxt(pcaMatrixPath)
print("Pca matrix shape", pcaMatrix.shape)
print("Loading scaler...")
scaler = StandardScaler().fit(trainData.iloc[:,8:].values)
print("Loaded!")

trainSpeakers = np.loadtxt(trainSpeakersPath)

# Start computing KLD between the test speaker and all the train speakers

KLDs = {}
variances = {}
for trainSpeaker in trainSpeakers:
    trainSpeaker = int(trainSpeaker)
    KLD,variance = computeKLD(trainData,testData,testSpeaker,trainSpeaker,pcaMatrix,n_GMMs=500,n_components=10,scaler=scaler)
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


