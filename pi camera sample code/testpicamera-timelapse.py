from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(0,5):
	# sleep for 5 seconds
	sleep(5)
	# take a picture
	# change the file name on each iteration
	camera.capture(f'/home/pi/image{i}.jpg')

camera.stop_preview()