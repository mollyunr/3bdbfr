import numpy as np
import fnmatch
import os
import math
import sys
from sklearn import decomposition

#
# Takes [database_name test_user_number(1-40)] as arguments
#

arguments = len(sys.argv)

if arguments > 2:
    components = np.load('components_.npy')
    explained_variance = np.load('explained_variance_.npy')
    mean = np.load('mean_.npy')

    f = open('n_components__noise_variance.txt', 'rb')
    n_components = f.readline()
    n_components = int(float(n_components))
    noise_variance = f.readline()
    noise_variance = float(noise_variance)
    f.close()

    pca = decomposition.PCA(n_components = 0.8, copy = 'true')
    pca.components_ = components
    pca.explained_variance_ = explained_variance
    pca.mean_ = mean
    pca.n_components_ = n_components
    pca.noise_variance_ = noise_variance

    trainingFileNames = []

    path, dirs, files = os.walk(sys.argv[1]).next()
    for index in range(0, len(dirs)):
        path2, dirs2, files2 = os.walk(sys.argv[1] + '/' + dirs[index]).next()
        for indexTwo in range(0, len(files2)):
            trainingFileNames.append(sys.argv[1] + '/' + dirs[index] + '/' + files2[indexTwo])

    # locate all files in testing image directory
    testingFileNames = []

    for index in range(5, 10):
        testingFileNames.append('att_faces/s' + sys.argv[2] + '/' + str(index + 1) + '.pgm')

    # load all training images into list with unsigned integer (8 bit) values
    testingFaces = []
    for index in range(0, len(testingFileNames)):
        f = open(testingFileNames[index], 'rb')
        garbage = f.readline().split()
        image = np.fromfile(f,dtype = np.uint8)
        testingFaces.append(image)
        f.close()

    # transfer faces to numpy array
    testingFaces = np.array(testingFaces)

    # get eigenfaces for both testing and training data
    trainingEigenfaces = np.load('trainingEigenfaces.npy')
    testingEigenfaces = pca.transform(testingFaces)

    # initialize ROC curve variables
    falseNegatives = 0
    trueNegatives = 0
    truePositives = 0
    falsePositives = 0
    totalMatches = 0

    minimumSum = 0.0

    f = open('fr_results.txt', 'w')
    f.close()

    # loop for each testing face
    for index in range(0, len(testingEigenfaces)):
        error = []

        # find error for each training face compared to current testing face
        for indexTwo in range(0, len(trainingEigenfaces)):
            errorSum = 0.0
            vector = testingEigenfaces[index] - trainingEigenfaces[indexTwo]
            x = np.inner(vector, vector)
            errorSum = math.sqrt(x)
            error.append(errorSum)

        # find minimum error
        minimum = error[0]
        minIndex = 0
        for indexFour in range(1, len(error)):
            if error[indexFour] < minimum:
                minimum = error[indexFour]
                minIndex = indexFour
        totalMatches += 1

        f = open('fr_results.txt', 'a')

        # if error is less than threshold
        if minimum < 2000:
            f.write('positive\n')
            f.write(str(minimum) + '\n')
            f.write(testingFileNames[index][10:] + '\n')
            f.write(trainingFileNames[minIndex][14:] + '\n')
            f.write('\n')

        # if error is greater than threshold
        else:
            f.write('negative\n')
            f.write(str(minimum) + '\n')
            f.write(testingFileNames[index][10:] + '\n')
            f.write(trainingFileNames[minIndex][14:] + '\n')
            f.write('\n')

        f.close()
