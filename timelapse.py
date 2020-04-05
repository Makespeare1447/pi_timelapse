from time import sleep
import picamera

delay = 15

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    for filename in camera.capture_continuous('pics/img{timestamp:%H-%M-%S-%f}.jpg'):
        sleep(delay)
