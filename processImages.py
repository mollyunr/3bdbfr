import sys
import cv2
import os

def deletePictures(directory):
    path, dirs, files = os.walk(directory).next()
    for index in range(0, len(files)):
        if files[index].find('.png') > -1:
            os.remove(directory + '/' + files[index])

def crop(directory):
    # face detection
    path, dirs, files = os.walk(directory).next()
    for index in range(0, len(files)):
        if files[index].find('.png') > -1:
            image = cv2.imread(directory + '/' + files[index])
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faceClassifier = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml')
            faces = faceClassifier.detectMultiScale(grayImage, 1.2, 5)

            for x, y, w, h in faces:
                image2 = grayImage[y:y+h, x:x+h]
                image2 = cv2.resize(image2, (250, 250))
                cv2.imwrite(directory + '/' + str(index+1) + '.pgm', image2)
    
    deletePictures(directory)

if __name__ == '__main__':
    crop(sys.argv[1])
