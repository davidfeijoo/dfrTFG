import pickle
import numpy as np
from datetime import datetime
from numpy import linalg 
from sklearn.preprocessing import StandardScaler


# Choose pc of variance or n components to keep after PCA

criterion = 'pc' #'pc' or 'ncomp'

if criterion == 'pc': 
    minPC = 57.9 
    minNComp = None
elif criterion == 'ncomp':
    minPC = None
    minNComp = 10
else: raise Exception('Choose pc or ncomp criterion')


globalFMPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/newFeatures/newGlobalFM.txt'

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nLoading global feature matrix...:  {current_time}")

globalFM = np.loadtxt(globalFMPath)

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"\nLoaded!!!:  {current_time}\n")

# Standarisation: the appropiate for pca as it makes the principal components decision independent from the units
scaler = pickle.load(open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/scaler.pkl' ,mode = 'rb'))
globalFM = scaler.transform(globalFM)
print("Means before the scaler", scaler.mean_)
print("Variances before the scaler", scaler.var_)
print("Means: " ,globalFM.mean(axis=0),"\nSum means: ", sum(globalFM.mean(axis=0)))
print("Vars: ",globalFM.var(axis=0),"\nSum vars: ", sum(globalFM.var(axis=0)))

# Estimate the sample covariance matrix. Dimensions 6373x6373
now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"Start computing matrix q:  {current_time}")

Q = np.cov(globalFM.transpose()) #Transpose because the each row has to be a variable and each column a sample, Q is real

# Then we compute the eigenvectors of Q, selecting the ones with the highest eigenvalues, which are considered as the principal components (PCs).
now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"Start computing eigenvalues:  {current_time}")

eigVal,eigVec = linalg.eigh(Q) # Each column is an eigenVector, using eigh (for covariance matrixes) always returns real values

# Sorting the eigenvectors in descending order of eigenvalues

now1 = datetime.now()
current_time = now1.strftime("%H:%M:%S")
print(f"Sorting eigenVectors:  {current_time}")

sorted_index = np.argsort(eigVal)[::-1] 
sorted_eigVal = eigVal[sorted_index]
sorted_eigVec = eigVec[:,sorted_index] # Dimensions 6373 x 6373

# We use the 10 most important dimensions
n_components = 0
pcaMatrix = 0
for n_components in range(80):
    pcaMatrix = sorted_eigVec[:,0:n_components]  # Dimensions 6373 x 10

    # Percentage of explained variance per principal component:
    explained_variances = []
    for i in range(len(sorted_eigVal)):
        explained_variances.append(sorted_eigVal[i] / np.sum(eigVal))
    print(f"Sum of explained variances = {np.sum(explained_variances)}\nExplained_variances [0:{n_components}] = {explained_variances[0:n_components]}\nSum of explained variances [0:{n_components}] = {np.sum(explained_variances[0:n_components])}\n")
    if minPC != None:
        if np.sum(explained_variances[0:n_components]) >= minPC/100: break # for 57.9% of the variance
    if minNComp != None:
        if n_components == minNComp: break # For the 10 principal components 35.45% of the variance

# Saving the matrix in a file
print("Saving the pca matrix")
pcaMatrixPath = f'/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/newFeatures/newPcaMatrix{n_components}.txt'
print("PCA Matrix:\n", pcaMatrix)
np.savetxt(pcaMatrixPath,pcaMatrix)
print("Saved \n")
