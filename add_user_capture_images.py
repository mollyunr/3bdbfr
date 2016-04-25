import pygame.camera
import pygame.image
import sys
import os
import errno
import time

arguments = len(sys.argv)

action = 'add_user'
user = sys.argv[1]
password = sys.argv[2]
privileges = sys.argv[3]
database_name = sys.argv[4]

pygame.camera.init()
cameras = pygame.camera.list_cameras()
print "avaiable cameras", cameras
print "Using camera %s" % cameras[0]
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(1000,800))

#Make directory
if os.path.exists(database_name):
	directory = database_name + "/" + user + "/"
	if not os.path.exists(directory):
	    os.makedirs(directory)

	raw_input("Waiting for button click...")
	cam.start()

	image = cam.get_image()
	pygame.image.save(image, directory+"/photo1.png")
	time.sleep(0.5)

	image = cam.get_image()
	pygame.image.save(image, directory+"/photo2.png")
	time.sleep(0.5)

	image = cam.get_image()
	pygame.image.save(image, directory+"/photo3.png")
	time.sleep(0.5)

	image = cam.get_image()
	pygame.image.save(image, directory+"/photo4.png")
	time.sleep(0.5)

	image = cam.get_image()
	pygame.image.save(image, directory+"/photo5.png")
	time.sleep(0.5)

	if( image != 0 ):
	    print "Picture taken"
	if( image == 0 ):
	    print "Picture NOT taken"
	pygame.camera.quit()
else:
	print "Database does not exist"
