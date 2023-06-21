import numpy as np
import pickle
import pandas as pd
from datetime import datetime
import os
import audiofile

test_speakers = list(map(int,np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')))

# Get the dictionary with the close speakers to each test speaker
is_plain = False
pc = 58
print("\n% variance:", pc)
# Define the approach: 1 -> Unique speaker, 2 -> Oversampling, 3 -> Weighting
approach = 1
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

print("Selected approach: Unique Speaker")


#   1: Load the sentences from the training speakers

trainDataPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/trainData.feather'
audioFolderPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/Audio'

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print(f"\nLoading train dataset...:  {current_time}\n")
trainData = pd.read_feather(trainDataPath)
print(trainData)
print(f"Number of samples in train dataset:", len(trainData))



minSeconds = 200/N
print(f"Minimum of seconds: {minSeconds} seconds per train speaker in the adaptation sets")

for speaker in test_speakers:
    print(f"Building set for speaker {speaker}")

    adaptationSetPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{folder}/individual/adaptation{speaker}Data.feather'
    durationsPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/database/{folder}/individual/length{speaker}Unique.pkl'

    adap_speakers = closeSpeakersDIC[speaker][0:N]

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


            if 20*i < N: # Save only every 20 speakers to avoid handling big dataframes
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
        print("Mean duration per speaker: ", totalDuration/N)

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



