import numpy as np
import pickle


testSpeakers = np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')
# trainSpeakers = np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/trainSpeakersList.txt')
speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/plain/closeSpeakersFeaturesStandardScaler.pkl'
with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

numberSentences = {}

testSpeakers = list(map(str,(list(map(int,testSpeakers)))))

for speaker in dic.keys():
    if speaker in testSpeakers:
        numberSentences[speaker] = dic[speaker].shape[0]

speakerLeastSentences = min(numberSentences, key=lambda k: numberSentences[k])
min_sentences = numberSentences[speakerLeastSentences]
speakerMostSentences = max(numberSentences, key=lambda k: numberSentences[k])
max_sentences = numberSentences[speakerMostSentences]

print("Minimum number of sentences:", min_sentences,"for speaker", speakerLeastSentences)
print("Maximum number of sentences:", max_sentences,"for speaker", speakerMostSentences)

print(numberSentences)

