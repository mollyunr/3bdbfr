import numpy as np
import cv2
import sys

# to run: python detect.py <image_name>

class image:

	def __init__(self, filename):
		self.imageFile = filename
		self.classifierPath = '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml'

	def readImageFromFile(self):
		self.uncropped = cv2.imread(self.imageFile)
		try:
			self.uncropped
		except NameError:
			print "Could not read image from " + self.imagefile + ".\n"

	def detectFace(self):
		# get the face classifier from openCV library
		faceClassifier = cv2.CascadeClassifier(self.classifierPath)
		
		# can only detect faces in grayscale images
		grayImage = cv2.cvtColor(self.uncropped,cv2.COLOR_BGR2GRAY)
		self.faceCoords = faceClassifier.detectMultiScale(grayImage, 1.2, 5)

		# check to see if face was detected
		if self.faceCoords == ():
			print "Face not detected. Try Again."
			return False
		else:
			return True

	def cropImage(self):
		try:
			for(x,y,w,h) in self.faceCoords:
				self.croppedImage = self.uncropped[y:y+h, x:x+w]
		except AttributeError:
			print "could not crop image.\n"

	def writeCroppedImage(self):
		self.imageFile = self.imageFile.split('.')
		croppedFileName = self.imageFile[0] + "cropped." + self.imageFile[1]
		cv2.imwrite(croppedFileName, self.croppedImage)
		
	def showImage(self, title):
		cv2.imshow(title,self.croppedImage)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	
if __name__ == '__main__':
	detect = image(sys.argv[1])
	detect.readImageFromFile()
	if detect.detectFace():
		detect.cropImage()
		detect.writeCroppedImage()
		detect.showImage('image')

