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
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(100,100))

#Make directory
if not os.path.exists(user):
    os.makedirs(user)

raw_input("Waiting for button click...")
cam.start()

image = cam.get_image()
pygame.image.save(image, user+"/photo1.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, user+"/photo2.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, user+"/photo3.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, user+"/photo4.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, user+"/photo5.png")
time.sleep(0.5)

if( image != 0 ):
    print "Picture taken"
if( image == 0 ):
    print "Picture NOT taken"
pygame.camera.quit()
