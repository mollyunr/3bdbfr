import pygame.camera
import pygame.image
import sys
import os
import errno
import time
import StringIO
import shutil
from select import select

SIZE = (300,300)
CAM_INDEX = 0

def timer(timeout):
	rlist, _, _ = select([sys.stdin], [], [], timeout)
	if rlist:
	    s = sys.stdin.readline()
	    return s

def initializeCamera(index):
	pygame.camera.init()
	cam = 0
	#use default webcam
	cam = pygame.camera.Camera(pygame.camera.list_cameras()[index],SIZE)
	
	#check if webcam detected, if not report error message
	return cam

def initializeScreen(cam):
	img = cam.get_image()
	width = img.get_width()
	height = img.get_height()
	screen = pygame.display.set_mode((width,height))
	return screen


def takePictures(cam, directory):
	count = 0 
	while count < 5:
		delay = timer(1)
		img = cam.get_image()		
		pygame.image.save(img, directory+"/"+str(count)+".png")
		count += 1

def getTestPictures(directory):
	camera = initializeCamera(CAM_INDEX)
	camera.start()

	user_directory = directory
	if not os.path.exists(user_directory):
		os.mkdir(user_directory)

	takePictures(camera, user_directory)

if __name__ == '__main__':
    camera()
