import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    camera.start_recording('foo.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_recording()