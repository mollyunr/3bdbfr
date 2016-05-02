import numpy as np
import cv2
import fnmatch
import os
import math
import sys
from sklearn import decomposition

#
# Takes [test_folder_name database_name username] as arguments
#
def testPCA(test_folder_name, database_name, username):

    print username

    # face detection
    path, dirs, files = os.walk(test_folder_name).next()
    for index in range(0, len(files)):
        if files[index].find('.png') > -1:
            image = cv2.imread(test_folder_name + '/' + files[index])
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faceClassifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
            faces = faceClassifier.detectMultiScale(grayImage, 1.2, 5)

            for x, y, w, h in faces:
                image2 = grayImage[y:y+h, x:x+h]
                image2 = cv2.resize(image2, (250, 250))
                cv2.imwrite(test_folder_name + '/' + str(index+1) + '.pgm', image2)

    components = np.load('components_.npy')
    explained_variance = np.load('explained_variance_.npy')
    mean = np.load('mean_.npy')

    f = open('n_components__noise_variance.txt', 'rb')
    n_components = f.readline()
    n_components = int(float(n_components))
    noise_variance = f.readline()
    noise_variance = float(noise_variance)
    f.close()

    pca = decomposition.PCA(n_components = 0.95, copy = 'true')
    pca.components_ = components
    pca.explained_variance_ = explained_variance
    pca.mean_ = mean
    pca.n_components_ = n_components
    pca.noise_variance_ = noise_variance

    trainingFileNames = []
    fileType = '.pgm'

    path, dirs, files = os.walk(database_name + '/' + username).next()
    for index in range(0, len(files)):
        trainingFileNames.append(database_name + '/' + username + '/' + files[index])

    traininFaces = []

    for index in range(0, len(trainingFileNames)):
        f = open(trainingFileNames[index], 'rb')
        garbage = f.readline().split()
        image = np.fromfile(f, dtype = np.uint8)
        traininFaces.append(image)
        f.close()

    traininFaces = np.array(traininFaces)

    # locate all files in testing image directory
    testingFileNames = []

    path, dirs, files = os.walk(test_folder_name).next()
    for index in range(0, len(files)):
        if files[index].find(fileType) > -1:
            testingFileNames.append(test_folder_name + '/' + files[index])

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
    trainingEigenfaces = pca.transform(traininFaces)
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
            f.write(testingFileNames[index] + '\n')
            f.write(trainingFileNames[minIndex] + '\n')
            f.write('\n')

        # if error is greater than threshold
        else:
            f.write('negative\n')
            f.write(str(minimum) + '\n')
            f.write(testingFileNames[index] + '\n')
            f.write(trainingFileNames[minIndex] + '\n')
            f.write('\n')

        f.close()

if __name__ == '__main__':
    testPCA(sys.argv[1],sys.argv[2],sys.argv[3])
