import numpy as np


test_speakers = list(map(int,np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/testSpeakersList.txt')))

test_list = ['plain','diverse']
pcs = [35,58]
attributes = ['arousal','dominance','valence']

for plain in test_list:
    print("\nPlain or diverse:", plain)
    for pc in pcs:
        print("% variance:",pc)
        for attribute in attributes:
            print("Attribute:",attribute)
            CCCdev = 0
            CCCadap = 0
            for speaker in test_speakers:
                CCCs = np.loadtxt(f'/Users/davidfeijoo/bussoImplementation/models/adaptation/individual/results/{plain}/{pc}pc/{attribute}/speaker_{str(speaker)}_{str(attribute)}_ccc.txt')
                CCCdev += CCCs[0]
                CCCadap += CCCs[1]
            print("Mean CCC for best development loss: ", CCCdev/60)
            print("Mean CCC for best adap loss: ", CCCadap/60)

