
from picamera import PiCamera

camera = PiCamera()

# set the size of the preview window
camera.resolution = (640,480)

camera.start_preview()

# Start recording video and save it to a file in h264 format.
# A utility can be used later to convert h264 to mp4 format.
camera.start_recording('/home/pi/video.h264')

# keep recording for 10 seconds
camera.wait_recording(10)

camera.stop_recording()

camera.stop_preview()