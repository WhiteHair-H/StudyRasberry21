import cv2

#setup video capture
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

while True:
    ret,img = cam.read()
    cv2.imshow('Video Capture', img)
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord(' '):
        cv2.imwrite('capture.jpg', img)
