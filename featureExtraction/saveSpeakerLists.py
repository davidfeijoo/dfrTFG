import csv
import numpy as np

leerTest1 = False
leerTrain = False
leerDev = False
leerTest2 = False
test1Speakers = []
test2Speakers = []
trainSpeakers = []
devSpeakers = []


with open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/particiones_e_IDs_csv.txt') as partition:
        csv_reader = csv.reader(partition, delimiter=';')
        for row in csv_reader:
            speakerID = row[0]


            if leerDev == True:
                devSpeakers.append(int(speakerID))
            if leerTest1 == True:
                test1Speakers.append(int(speakerID))
            if leerTest2 == True:
                test2Speakers.append(int(speakerID))
            if leerTrain == True:
                if speakerID == 'Unknown':
                    trainSpeakers.append(speakerID)
                else:
                    trainSpeakers.append(int(speakerID))
            
            if row[0] == 'Development': leerDev = True
            if row[0] == 'Test1': leerTest1 = True
            if row[0] == 'Test2': leerTest2 = True
            if row[0] == 'Train': leerTrain = True
            if row[0] == '1295': leerDev = False
            if row[0] == '976': leerTest1 = False
            if row[0] == '1285': leerTest2 = False
            if row[0] == 'Unknown': leerTrain = False

np.savetxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/developmentSpeakersList.txt',devSpeakers)
np.savetxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/trainSpeakersList.txt',trainSpeakers)
np.savetxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt',test1Speakers)