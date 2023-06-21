import numpy as np
import pickle
from datetime import datetime


from computeKLD import computeKLD


speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesConUnknown.pkl'
pcaMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/pcaMatrixSKLEARNfromStandardScaler.txt'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoading dictionary of train and test speakers' features and pcaMatrix:  {current_time}\n")

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)
pcaMatrix = np.loadtxt(pcaMatrixPath)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Loaded!:  {current_time}\n")

speakers = [2,10,15]

KLDs = []

for speaker in speakers:
    KLD = computeKLD(dic,2,speaker,pcaMatrix)

