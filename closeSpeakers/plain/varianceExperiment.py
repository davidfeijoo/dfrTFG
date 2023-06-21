import numpy as np
from sklearn.decomposition import PCA

print("Loading matrix...")
globalFM = np.loadtxt('/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/globalFMmean0.txt')
print("Loaded!")

variances = globalFM.var(axis = 0)
maxVar = max(variances)
idx = list(variances).index(maxVar)
print("Variance of globalFM", variances)
print("Maximum variance", maxVar )
print("Index of max variance", idx)

pca = PCA(n_components=10)
pca.fit_transform(globalFM)
pcaMatrix = pca.components_
print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))

