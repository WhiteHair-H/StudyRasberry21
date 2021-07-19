import cv2

cam = cv2.VideoCapture(0) # 기본 캠
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 창 높이

fourcc = cv2.VideoWriter_fourcc(*'XVID') # XVID 비디오 코덱
is_record = False #녹화상태

while True:
    ret, img = cam.read() # 웹캠 읽기
    cv2.imshow('Video Capture' , img) # 카메라 영상 CAM이라는 이름으로 창을 띄움
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('c'): # q를 입력받으면
        cv2.imwrite('./Capture/capture.jpg', img)
        print('이미지 캡처 완료')
    elif key == ord('r') and is_record == False: # r을 입력하면 최초 레코딩 시작
        is_record = True
        video = cv2.VideoWriter('./Capture/record.avi', fourcc, 20, (img.shape[1], img.shape[0]))
        print('녹화 시작')
    elif key == ord('r') and is_record == True: # 녹화중
        is_record = False
        video.release()
        print('녹화 종료')

    if is_record == True: # 현재화면 녹화
        video.write(img)

cam.release()
cv2.destroyAllWindows()
