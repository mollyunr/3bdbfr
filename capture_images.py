import pygame.camera
import pygame.image
import sys
import os
import errno
import time


pygame.camera.init()
cameras = pygame.camera.list_cameras()
print "avaiable cameras", cameras
print "Using camera %s" % cameras[0]
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(1000,1000))

#Make directory
if not os.path.exists("test_photos"):
    os.makedirs("test_photos")

raw_input("Waiting for button click...")
cam.start()

image = cam.get_image()
pygame.image.save(image, "test_photos/photo1.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, "test_photos/photo2.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, "test_photos/photo3.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, "test_photos/photo4.png")
time.sleep(0.5)

image = cam.get_image()
pygame.image.save(image, "test_photos/photo5.png")
time.sleep(0.5)

if( image != 0 ):
    print "Picture taken"
if( image == 0 ):
    print "Picture NOT taken"
pygame.camera.quit()
