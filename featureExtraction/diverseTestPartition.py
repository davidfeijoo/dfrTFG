import json
import numpy as np
import pandas as pd
import os
import audiofile
from datetime import datetime

from featureExtraction import load_features

pathLabels ='/Users/davidfeijoo/bussoImplementation/MSP_podcast/Labels/labels_consensus.json'
audioPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio'
testSpeakersList = list(map(int,np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')))


# Opening JSON file and loading it to a dataframe
with open(pathLabels) as json_file:
    data = json.load(json_file) # Python Dictionary with labels for each audio

dataframe = pd.DataFrame(data).T

# Create a new df with only the audios of the test set speakers
testData = dataframe.loc[dataframe['Split_Set'] == 'Test1']
testData.reset_index(inplace=True)
testData = testData.rename(columns = {'index':'Audio'})
print("\n\nTest dataframe\n",testData)

# Initialize new dataframes for test A and test B
testAdf = pd.DataFrame()
testBdf = pd.DataFrame()

# For each speaker get utterances randomly until 200s and keep adding them to the new test A dataframe
minSeconds = 200
i = 0
for speaker in testSpeakersList:
    D = 0
    nsamples = 0

    speakerData = testData.loc[testData['SpkrID'] == str(speaker)]

    while D <= minSeconds:
        sample = speakerData.sample(n=1)
        audio = str(sample.iloc[0,0])
        if audio not in testAdf.values: # Check that samples are not repeated
            audioFile = os.path.join('/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio', audio) # Gives the path to the os joining with a '/' both arguments
            signal, sampling_rate = audiofile.read(audioFile)
            duration = audiofile.duration(audioFile)
            D += duration
            nsamples +=1
            testAdf = pd.concat([testAdf,sample],ignore_index=True)
            
    i+=1 


testBdf = testData.merge(testAdf.drop_duplicates(), how='left',indicator=True)
testBdf = testBdf.loc[testBdf['_merge'] == 'left_only']
testBdf.drop(columns=['_merge'],inplace=True)
testBdf.reset_index(inplace=True)
testBdf.drop(columns=['index'],inplace=True)

print("\n\nTest A dataframe\n",testAdf)
print("\n\nTest B dataframe\n",testBdf)

# Load the archives
now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nLoading old test A,B df...:  {current_time}")

oldA = pd.read_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/testAData.feather')
oldB = pd.read_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/testBData.feather')

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nLoaded!:  {current_time}")

# Check which audios are in each old df and keep them
audiosA = testAdf['Audio'].tolist()
audiosB = testBdf['Audio'].tolist()

newAA = oldA.loc[oldA['Audio'].isin(audiosA)]
newAB = oldB.loc[oldB['Audio'].isin(audiosA)]
newA = pd.concat([newAA,newAB],ignore_index=True)

newBA = oldA.loc[oldA['Audio'].isin(audiosB)]
newBB = oldB.loc[oldB['Audio'].isin(audiosB)]
newB = pd.concat([newBB,newBA],ignore_index=True)

# Save the new test A and test B
now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nSaving feathers!:  {current_time}")


print("New A",newA)
print("New B",newB)
newA.to_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestA.feather')
newB.to_feather('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/newTestB.feather')

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nSaved!:  {current_time}\n")