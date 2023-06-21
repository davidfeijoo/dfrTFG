import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.mixture import GaussianMixture
from scipy.stats import norm


def computeKLD(trainDF,testDF,testSpeakerID,trainSpeakerID, pcaMatrix,n_GMMs = 100,n_components = 10,scaler = None):
    print("Number of times the GMMs are fitted:", n_GMMs)
    testSpeakerID = str(int(testSpeakerID))
    trainSpeakerID = str(int(trainSpeakerID))
    fM1 = testDF.loc[testDF['SpkrID'] == testSpeakerID].iloc[:,8:].to_numpy()
    fM1 = fM1.astype(float)
    size1 = fM1.shape[0]
    fM2 = trainDF.loc[trainDF['SpkrID'] == trainSpeakerID].iloc[:,8:].to_numpy()
    fM2 = fM2.astype(float)
    size2 = fM2.shape[0]
    
    # Standardize
    if scaler != None:
        fM1 = scaler.transform(fM1)
        fM2 = scaler.transform(fM2)

    testSentencesProjection = np.dot(fM1,pcaMatrix) # Matriz de features del speaker test Mx6373 x 6373x10 = Mx10
    trainSentencesProjection = np.dot(fM2, pcaMatrix) # Matriz de features del train speaker train

    print(f"\nNumber of sentences speaker {testSpeakerID}: ",testSentencesProjection.shape[0])
    print(f"Number of sentences speaker {trainSpeakerID}: ",trainSentencesProjection.shape[0],"\n")

    n_samples_MC = 5000

    # For every speaker choose the best number of components for the GMM
    scores = []
    sigma = 0
    minimum = 25
    if size1 < minimum:
        print(f"F Test speaker {testSpeakerID} has less than {minimum} samples ({size1} samples). It is not possible to fit a GMM with {n_components} components")
        KLD = np.inf

    elif size2 < minimum:
        print(f"F Train speaker {trainSpeakerID} has less than {minimum} samples ({size2} samples). It is not possible to fit a GMM with {n_components} components")
        KLD = np.inf
    else:
        for n in range(n_GMMs):

            # Randomly select 25 sentences of each speaker
            idx1 = list(np.random.choice(size1,size=25,replace=False))
            idx2 = list(np.random.choice(size2,size=25,replace=False))
            chosenTest = testSentencesProjection[idx1,:]
            chosenTrain = trainSentencesProjection[idx2,:]
            size1 = 25
            size2 = 25

            if n == 0:
                print(f"Number of selected sentences speaker {testSpeakerID}: ",size1)
                print(f"Number of selected sentences speaker {trainSpeakerID}: ",size2)

            # Fixed number of components

            # Create the first GMM for fitting the test speaker's sentences
            GMMTestSpeaker = GaussianMixture(n_components=n_components,reg_covar=1e-6,n_init = 1) 
            GMMTestSpeaker.fit(chosenTest)

            #Then create the second GMM
            GMMTrainSpeaker = GaussianMixture(n_components=n_components,reg_covar=1e-6,n_init = 1)
            GMMTrainSpeaker.fit(chosenTrain)

            # Monte-carlo simulation
            
            test_samples = GMMTestSpeaker.sample(n_samples_MC)[0]

            score1 = GMMTestSpeaker.score_samples(test_samples)
            score2 = GMMTrainSpeaker.score_samples(test_samples)
            # print(f"\nScore1: {score1} \nScore2: {score2}\n")

            scores.append(np.mean(score1-score2))


        # Prueba para poner como kld la media de la gaussiana
        mu, sigma = norm.fit(scores)
        KLD = mu

        print(f"\nKLD speaker {testSpeakerID} and {trainSpeakerID}: {KLD}\n")

    # return KLD,vars
    return KLD , sigma**2



