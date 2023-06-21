import pickle
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


speakerID = str(20)

# Load the necessary for doing the projections
speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesMinMaxScaler.pkl'
pcaMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/pcaMatrix.txt'

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

pcaMatrix = np.loadtxt(pcaMatrixPath)

# Get the sentences from the speaker

speakerSentences = dic[speakerID] # Mx6373

# Project the sentences to the new speace 

projection = np.dot(speakerSentences,pcaMatrix) # Mx3 o Mx10



# PLOT

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

for row in projection:
    print(row)
    ax.scatter(row[0],row[1],row[2])

ax.set_title('3D Parametric Plot')
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)

plt.show()

