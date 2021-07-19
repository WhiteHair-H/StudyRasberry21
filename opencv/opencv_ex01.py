import cv2
# 오픈소스 기본소스

cam = cv2.VideoCapture(0) # 기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 창 높이

while True:
    ret, img = cam.read() # 웹캠 읽기
    cv2.imshow('Video Capture' , img) # 카메라 영상 CAM이라는 이름으로 창을 띄움
    key = cv2.waitKey(10)
    if key == 27:
        break
    if key == ord('q'): # q를 입력받으면
        cv2.imwrite('capture.jpg', img)

cam.release()
cv2.destroyAllWindows()
