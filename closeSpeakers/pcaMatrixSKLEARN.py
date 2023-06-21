import pickle
import numpy as np
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler



def pcaMatrixSKL():

    gadi = False

    if gadi:
        globalFMPath = 'globalFM.txt'
        pcaMatrixPath = 'pcaMatrix.txt'
    else:
        globalFMPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/globalFM.txt'
        pcaMatrixPath = '/Users/davidfeijoo/bussoImplementation/MSP_podcast/closeSpeakers/pcaMatrix.txt'


    now1 = datetime.now()
    current_time = now1.strftime("%H:%M:%S")
    print(f"\nLoading global feature matrix...:  {current_time}")

    globalFM = np.loadtxt(globalFMPath)
    print(globalFM)

    now1 = datetime.now()
    current_time = now1.strftime("%H:%M:%S")
    print(f"\nLoaded!!!:  {current_time}")

    # Standarization
    scaler = pickle.load(open('/Users/davidfeijoo/bussoImplementation/MSP_podcast/feathers/scaler.pkl' ,mode = 'rb'))
    globalFM = scaler.transform(globalFM)
    print("Means: " ,globalFM.mean(axis=0),"\nSum means: ", sum(globalFM.mean(axis=0)))
    print("Vars: ",globalFM.var(axis=0),"\nSum vars: ", sum(globalFM.var(axis=0)))

    now1 = datetime.now()
    current_time = now1.strftime("%H:%M:%S")
    print(f"Start computing PCA matrix:  {current_time}")

    # To compute the transformation matrix:
    pca = PCA(n_components=10)
    pca.fit_transform(globalFM)
    pcaMatrix = pca.components_.transpose()
    print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))
    print('Sum of explained variances =', sum(pca.explained_variance_ratio_))
    print("pcaMatrix: ", pcaMatrix)
    print("Number of features in: ", pca.n_features_in_)

    # Saving the matrix in a file
    # np.savetxt(pcaMatrixPath,pcaMatrix)

    return pcaMatrix
