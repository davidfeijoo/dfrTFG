import numpy as np
import pickle


# Este código es para correr en local ya para juntar todas las listas de closest speakers

pc = 35
plain = 'plain'
if plain == 'plain': folder = 'Intento 2'
elif plain == 'diverse': folder = 'Intento 3'
else: raise Exception('\nNot existing option, choose plain or diverse\n')

testSpeakers = list(map(int,np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')))

globalDict = {}

for testSpeaker in testSpeakers:

    lista = list(map(int,np.loadtxt(f'/Users/davidfeijoo/bussoImplementation/Close speakers selection/{folder}/KLDs/KLDs_{pc}pc/closestSpeakers_testSpeaker_'+str(testSpeaker)+'.txt')))
    globalDict[testSpeaker] = lista
    print(lista[0:5])



with open(f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/{plain}/KLDs_{pc}pc_{plain}/closestSpeakers_{pc}pc.pkl',mode = 'wb') as pkl_speakerFile:
    pickle.dump(globalDict,pkl_speakerFile)


    


