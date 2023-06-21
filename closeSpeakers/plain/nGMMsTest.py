import numpy as np
import pickle
from datetime import datetime
import matplotlib.pyplot as plt


from computeKLD import computeKLD


speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesConUnknown.pkl'
transMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/transMatrixAntigua.txt'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoading dictionary of train and test speakers' features:  {current_time}\n")

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"Loaded!:  {current_time}\n")

tM = np.loadtxt(transMatrixPath)

n_GMMs = np.arange(10,200,10)
# n_GMMs = 10,20
speakers = [2,10,15]

for speaker in speakers:
    KLDs = []
    for n in n_GMMs:
        KLD = computeKLD(dic,2,speaker,tM,n_GMMs=n)
        KLDs.append(KLD)

    # Plot 1: 
    plt.plot(n_GMMs,KLDs)
    plt.xlabel('Number of GMMs')
    plt.ylabel('KLD')
    plt.title(f'KLD (n GMMs) speaker {speaker}')
    plt.show()
