from approaches import uniqueSpeaker, oversampling
import pickle
import audiofile
from datetime import datetime
import pandas as pd
import numpy as np
import os


# Get the dictionary with the close speakers to each test speaker
is_plain = True
pc = 35
print("\n% variance:", pc)
# Define the approach: 1 -> Unique speaker, 2 -> Oversampling, 3 -> Weighting
approach = 2
# Define the number of close speakers selected to each test speaker
N = 5


if is_plain:
    print("Selected test A: Plain")
    folder = f'plain/{pc}pc'
    closeSpeakersPath = f"/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/plain/KLDs_{pc}pc_plain/closestSpeakers_{pc}pc.pkl"
else:
    print("Selected test A: Diverse")
    folder = f'diverse/{pc}pc'
    closeSpeakersPath = f"/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/diverse/KLDs_{pc}pc_diverse/closestSpeakers_{pc}pc.pkl"


with open(closeSpeakersPath ,mode = 'rb') as pkl_speakerFile:
    closeSpeakersDIC = pickle.load(pkl_speakerFile)


if  approach == 1:
    print("Selected approach: Unique Speaker")
    adaptationSetPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{folder}/adaptationUniqueData.feather'
    durationsPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{folder}/lengthAdaptationUnique.pkl'
    adap_speakers = uniqueSpeaker(closeSpeakersDIC,N)
elif approach == 2:
    print("\nSelected approach: Oversampling")
    adaptationSetPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{folder}/adaptationOversamplingData.feather'
    durationsPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{folder}/lengthAdaptationOversampling.pkl'
    adap_speakers = oversampling(closeSpeakersDIC,N)
else:
    adap_speakers = []
    adaptationSetPath = 'ERROR'
    durationsPath = 'ERROR'
    raise Exception("Sorry, choose approach 1 (unique speaker) or 2 (oversampling)")

adap_speakers = list(adap_speakers)
adap_speakers.sort()
setLength = len(adap_speakers)

print("\nResulting set is:\n")
print(f" {adap_speakers} \n")
print(f"Length of the set: {setLength}\n")

# Check the path
# d = {'col1': [1, 2], 'col2': [3, 4]}
# pd.DataFrame(d).to_feather(adaptationSetPath)


# Balance sampling criterion that aims to select approximately the same amount of data for each speakers. 
# X seconds per speaker in the test set. (X = 50,100,150,200s)
# Approximately X*60/setLength s per train speaker 

minSeconds = 200*60/setLength
print(f"Minimum of seconds: {minSeconds} seconds per train speaker in the adaptation set")

#   1: Load the sentences from the training speakers

trainDataPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/trainData.feather'
audioFolderPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio'

# # For Faster testing
# adapSet = np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')
# trainDataPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/testAData.feather'
# setLength = len(adapSet)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoading train dataset...:  {current_time}\n")
trainData = pd.read_feather(trainDataPath)
print(trainData)
print(f"Number of samples in train dataset:", len(trainData))

# 2: For each speaker in the adaptation set pick their sentences and randomly select D = 200*60/setLength s per speaker
adaptationData = pd.DataFrame(columns=trainData.columns)
temporal = pd.DataFrame(columns=trainData.columns)
totalDuration = 0
totalSamples = 0
numAndTime = {}
i= 0
prevSpeaker = 0
speakerTimes = 0
for speaker in adap_speakers:
    D = 0
    nsamples = 0
    speaker = int(speaker)
    data = trainData.loc[trainData['SpkrID'] == str(speaker),:]

    if speaker != prevSpeaker: speakerTimes = 1
    else: speakerTimes +=1

    whiles = 0
    while D < minSeconds: # Randomly pic audios until getting D s
        whiles +=1
        print(f"Number of whiles speaker {speaker}: {whiles}")
        sample = data.sample(n=1)
        # print("Sample:\n", sample)
        audio = str(sample.iloc[0,0])
        if audio not in temporal.values: # check that the audio is not repeated
            audioFile = os.path.join('/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio', audio) # Gives the path to the os joining with a '/' both arguments
            signal, sampling_rate = audiofile.read(audioFile)
            duration = audiofile.duration(audioFile)
            temporal = pd.concat([temporal, sample], ignore_index=True)
            D += duration
            nsamples +=1
            # print("Temporal:\n", temporal)
            print("Duration of the sample:",duration)
            print(f"Number of samples added of speaker {speaker}:", nsamples)
            print(f"Total duration of speaker {speaker}", D)
        elif approach == 1: 
            print('Repeated sample! Not added')
            if whiles >= 100: break
        elif approach == 2:
            # Check how many times the audio is inside with respect to how many times the speaker appears in the list. If it's less than the times the speaker appears, add it again
            audio_counter = int(temporal.loc[temporal['Audio'] == audio].value_counts().to_numpy())
            print("Audio counter", audio_counter)
            if speakerTimes > audio_counter:
                print("Legal")
                audioFile = os.path.join('/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio', audio) # Gives the path to the os joining with a '/' both arguments
                signal, sampling_rate = audiofile.read(audioFile)
                duration = audiofile.duration(audioFile)
                temporal = pd.concat([temporal, sample], ignore_index=True)
                D += duration
                nsamples +=1
            else: print('Repeated sample in this turn! Not in')
 


    totalDuration +=D
    totalSamples +=1


    if 20*i < setLength: # Save only every 20 speakers to avoid handling big dataframes
        if speaker == adap_speakers[20*i]:
            adaptationData = pd.concat([adaptationData, temporal], ignore_index=True)
            temporal = pd.DataFrame(columns=trainData.columns)
            i += 1
            print("Adaptation set data \n", adaptationData)
    if speaker == adap_speakers[-1]: 
        adaptationData = pd.concat([adaptationData, temporal], ignore_index=True)
        temporal = pd.DataFrame(columns=trainData.columns)
        print("In second if")

    prevSpeaker = speaker
    numAndTime[speaker] = nsamples,D
    # print("Adaptation data: ",adaptationData)

print("Total samples of the adaptation:",totalSamples)
print("Total Duration of the adaptation:",totalDuration)
print("Mean duration per speaker: ", totalDuration/setLength)

# 3: Save the adaptation set

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nSaving data feather...:  {current_time}\n")

adaptationData.to_feather(adaptationSetPath)
with open(durationsPath,mode = 'wb') as pkl_speakerFile:
    pickle.dump(numAndTime,pkl_speakerFile)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nSaved data feather!:  {current_time}\n")

