import os
import fnmatch
import cv2

def updateFiles(inputFolder, outputFolder):
    path, dirs, files = os.walk(outputFolder).next()

    remFileNames = []
    for index in range(0, len(files)):
        remFileNames.append(outputFolder + '/' + files[index])

    for index in range(0, len(remFileNames)):
        if files[index].find('.pgm') > -1:
            os.remove(remFileNames[index])

    path, dirs, files = os.walk(inputFolder).next()

    fileNames = []
    for index in range(0, len(files)):
        fileNames.append(inputFolder + '/' + files[index])

    count = 0;
    for index in range(0, len(fileNames)):
        if count > 9:
            break
        if files[index].find('.png') > -1:
            count = count + 1
            image = cv2.imread(fileNames[index])
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faceClassifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml');
            faces = faceClassifier.detectMultiScale(grayImage, 1.2, 5)

            for x, y, w, h in faces:
                image2 = grayImage[y:y+h, x:x+h]
                image2 = cv2.resize(image2, (250, 250))
                cv2.imwrite(outputFolder + '/' + str(index) + '.pgm', image2)


if __name__ == '__main__':
    updateFiles('databases/user_database/mheadland/temp', 'databases/user_database/mheadland')
