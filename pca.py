import numpy as np
import fnmatch
import os
import math
import sys
from sklearn import decomposition

#
# Takes database name as argument
#

def runPCA(database):
    print "PCA!"
    trainingFileNames = []

    path, dirs, files = os.walk("databases/" + database).next()
    for index in range(0, len(dirs)):
        path2, dirs2, files2 = os.walk("databases/" + database + '/' + dirs[index]).next()
        for indexTwo in range(0, len(files2)):
            filename = "databases/" + database + '/' + dirs[index] + '/' + files2[indexTwo]
            if filename.find(".pgm") > -1:
                trainingFileNames.append(filename)

    # load all training images into list with unsigned integer (8 bit) values
    trainingFaces = []
    for index in range(0, len(trainingFileNames)):
        f = open(trainingFileNames[index], 'rb')
        garbage = f.readline().split()
        image = np.fromfile(f,dtype = np.uint8)
        trainingFaces.append(image)
        f.close()

    # transfer faces to numpy array
    trainingFaces = np.array(trainingFaces)

    # train PCA model with 95% detail retained, using training faces
    pca = decomposition.PCA(n_components = 0.95, copy = 'true')
    pca.fit(trainingFaces)

    # get eigenfaces for both testing and training data
    trainingEigenfaces = pca.transform(trainingFaces)

    np.save('components_', pca.components_)

    np.save('explained_variance_', pca.explained_variance_)

    np.save('mean_', pca.mean_)

    f = open('n_components__noise_variance.txt', 'w')
    f.write(str(pca.n_components_))
    f.write('\n')
    f.write(str(pca.noise_variance_))
    f.close()

    np.save('trainingEigenfaces', trainingEigenfaces)

if __name__ == '__main__':
    runPCA(sys.argv[1])
