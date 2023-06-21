import numpy as np
import pickle
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
from computeKLD import computeKLD


speakerID = str(2)

# Load the necessary for doing the projections
speakerFilePath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/closeSpeakersFeaturesMinMaxGlobal.pkl'
pcaMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/pcaMatrix.txt'

with open(speakerFilePath ,mode = 'rb') as pkl_speakerFile:
    dic = pickle.load(pkl_speakerFile)

pcaMatrix = np.loadtxt(pcaMatrixPath)

# Get the sentences from the speaker

speakerSentences = dic[speakerID] # Mx6373

# Project the sentences to the new speace 

projection = np.dot(speakerSentences,pcaMatrix) # Mx10

# Fit the GMMs of different numer of components and check de aic

lista = range(1,int(projection.shape[0]/2))
gmmAic = {}
gmmBic = {}

for ncomponents in lista:
    gmm = GaussianMixture(n_components=ncomponents,max_iter=100,tol=1e-3,n_init=50,init_params = 'random') # init_params = 'random' , n_init =20
    gmm.fit(projection)
    if(gmm.converged_):
        print(f'The gmm converged in {gmm.n_iter_}')
    gmmAic[gmm] = gmm.aic(projection),ncomponents
    gmmBic[gmm] = gmm.bic(projection),ncomponents
    print("Number of components:",ncomponents,"AIC:",gmmAic[gmm],"BIC", gmmBic[gmm])

bestModelAIC = min(gmmAic,key=lambda  k: gmmAic[k][0])
bestModelBIC = min(gmmBic,key=lambda  k: gmmBic[k][0])

print(f"\nSpeaker {speakerID}'s best model (AIC) is: \n")
print(bestModelAIC)
print("AIC =",gmmAic[bestModelAIC][0])
print("n components =",gmmAic[bestModelAIC][1],"\n")

print(f"Speaker {speakerID}'s best model (BIC) is: \n")
print(bestModelBIC)
print("BIC =",gmmBic[bestModelBIC][0],"\n")
print("n components =",gmmBic[bestModelBIC][1],"\n")



# Plot the AIC and BIC
aics = []
for i in gmmAic.values():
    aics.append(i[0])
bics = []
for i in gmmBic.values():
    bics.append(i[0])
plt.plot(lista,list(aics),label = f"AIC")
plt.plot(lista,list(bics),label = f"BIC")
plt.title(f'N components GMM - AIC/BIC speaker {speakerID}')
plt.xlabel('Number of components')
plt.ylabel('AIC / BIC')
plt.legend()
plt.show()

# Compute KLD

print("KLD best aic:",computeKLD(dic=dic,testSpeakerID=speakerID,trainSpeakerID=speakerID,pcaMatrix=pcaMatrix,n_GMMs=1,n_components=gmmAic[bestModelAIC][1]))
print("KLD best bic:",computeKLD(dic=dic,testSpeakerID=speakerID,trainSpeakerID=speakerID,pcaMatrix=pcaMatrix,n_GMMs=1,n_components=gmmBic[bestModelBIC][1]))