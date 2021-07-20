import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw , Image
from numpy.core.numeric import True_

# 카메라 기본 틀
# 영상 캡쳐 , 녹화
cap = cv2.VideoCapture(0) # 번호 0부터 +1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 수동 변환
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20)
# 영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') #H263
is_record = False # 녹화상태


# 무한루프 (q를 입력할때까지)
while True:
    ret , frame = cap.read() # 카메라 현재 영상 로드 , frame에 저장 , ret True/False
    # h , w , c = frame.shape
    # h , w , _ = frame.shape # c가 필요없을 때는
    h , w , _ = frame.shape # h, c가 필요없을 때는
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') # 파일이름에 :이 못들어가기때문 -> 20210720_164728

    if ret != True:break # ret이 false면 루프 탈출

    frame = Image.fromarray(frame) # 글자출력을 위해 변환
    draw = ImageDraw.Draw(frame) # 
    draw.text(xy=(10, (h - 40)) , text='실시간 웹캠 - {0}'.format(currDateTime) , font=font, fill=(0,0, 255))
    frame = np.array(frame) # 변환한 거 원상태로 복귀

    
    key = cv2.waitKey(1)
    if key == ord('q') : break # q를 입력하면 루프탈출
    elif key == ord('c'): # c는 화면캡처
        cv2.imwrite('./Capture/img_{0}.png'.format(fileDateTime), frame)
        print('이미지 저장 완료')
    elif key == ord('r'): #and is_record == False: # 레코드 시작
        is_record = True
        video = cv2.VideoWriter('./Capture/record_{0}.avi'.format(fileDateTime), fourcc, 20 , (w, h))
        print('녹화 시작')
    elif key == ord('t'): #and is_record == True_: # 레코드 종료
        is_record = False
        if 'video' in locals(): # video가 있는 지 찾으면 밑으로
            video.release() # 객체 해제
            print("녹화 완료")

    if is_record:
        video.write(frame)
        cv2.circle(img= frame , center=(620 , 15), radius=5, color=(0 , 0, 255) , thickness=3)

    cv2.imshow('RealTime CAM', frame) # 로드한 영상을 창에 띄움

cap.release() # 웹캠 해제
cv2.destroyAllWindows()