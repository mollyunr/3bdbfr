import os
import fnmatch

def update(inputFolder, outputFolder):
    path, dirs, files = os.walk(inputFolder).next()

    fileNames = []
    for index in range(0, len(files)):
        fileNames.append(inputFolder + '/' + files[index])

    for index in range(0, len(fileNames)):
        images = []
        if files[index].find('.png') > -1:
            image = cv2.imread(inputFolder + '/' + fileNames[index])
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faceClassifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml');
            faces = faceClassifier.detectMultiScale(grayImage, 1.2, 5)

            for x, y, w, h in faces:
                image2 = grayImage[y:y+h, x:x+h]
                image2 = cv2.resize(image2, (250, 250))
                images.append(image2)
                #cv2.imwrite(inputFolder + '/' + str(index) + '.pgm', image2)

        print images
if __name__ == '__main__':
    update('test_folder/temp', 'test_folder')
