import numpy as np
import pickle


# Este código es para correr en local ya para juntar todas las listas de closest speakers


testSpeakers = list(map(int,np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')))

globalDict = {}

for testSpeaker in testSpeakers:

    lista = list(map(int,np.loadtxt('/Users/davidfeijoo/bussoImplementation/Close speakers selection/Intento 2/KLD/KLDs_10comp_58pc/closestSpeakers_testSpeaker_'+str(testSpeaker)+'.txt')))
    globalDict[testSpeaker] = lista
    print(lista[0:5])



with open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/KLDs_10comp_58pc/closestSpeakers_10comp_58pc.pkl',mode = 'wb') as pkl_speakerFile:
    pickle.dump(globalDict,pkl_speakerFile)


    


