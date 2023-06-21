

def uniqueSpeaker(testSetDIC,N):
    # Each speaker in the test set generates a list with its closest speakers in the train set.
    # Since some speakers in the train set may be close to more than one speaker, 
    # the total number of selected speakers after combining the lists from the 50 speakers in the test set is less or equal to M = Nx60.
    adaptationSet = set()
    for list in testSetDIC.values():
        for speaker in list[0:N]:
            adaptationSet.add(speaker)
    
    return adaptationSet

def oversampling(testSetDIC,N):
    adaptationSet = []
    for list in testSetDIC.values():
        for speaker in list[0:N]:
            adaptationSet.append(speaker)
    adaptationSet.sort()
    return adaptationSet

def weighting():
    adaptationSet = []
    
    return adaptationSet