import cv2
import numpy as np

# 카메라 기본 틀
# 영상 자르기
cap = cv2.VideoCapture(0) # 번호 0부터 +1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 수동 변환
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 무한루프 (q를 입력할때까지)
while True:
    ret , frame = cap.read() # 카메라 현재 영상 로드 , frame에 저장 , ret True/False
    h , w, c = frame.shape
    crop = frame[: , :int(w/2)]

    if ret != True:break # ret이 false면 루프 탈출

    cv2.imshow('RealTime CAM', frame) # 로드한 영상을 창에 띄움
    cv2.imshow('Crop Result', crop)

    if cv2.waitKey(1) == ord('q'):break # q를 입력하면 루프탈출
        

cap.release() # 웹캠 해제
cv2.destroyAllWindows()