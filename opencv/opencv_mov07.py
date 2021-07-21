import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw , Image
from numpy.core.numeric import True_

## 함수 선언영역
def get_diff_image(frame_a , frame_b, frame_c , threshold):
    # 세개 모든 프레임을 회색으로 전환
    frame_a_gray = cv2.cvtColor(frame_a , cv2.COLOR_BGR2GRAY)
    frame_b_gray = cv2.cvtColor(frame_b , cv2.COLOR_BGR2GRAY)
    frame_c_gray = cv2.cvtColor(frame_c , cv2.COLOR_BGR2GRAY)

    # a/ b 사이 영상 차이값 , b/c 사이 영상 차이 값 구함
    diff_ab = cv2.absdiff(frame_a_gray , frame_b_gray) # 차이가 없음
    diff_bc = cv2.absdiff(frame_b_gray , frame_c_gray) # 차이값 있을수도 없을수도 있음

    # 영상 차이값이 40 이상이면 값을 흰색으로 바꿔줌
    ret, diff_ab_t = cv2.threshold(diff_ab,threshold, 255 , cv2.THRESH_BINARY)
    ret, diff_bc_t = cv2.threshold(diff_bc,threshold, 255 , cv2.THRESH_BINARY)

    # 두 영상에 공통된 부분은 1로 만듬
    diff = cv2.bitwise_and(diff_ab_t , diff_bc_t)
    
    # 영상에서 1이 된 부분은 확장(morpholy)
    k = cv2.getStructuringElement(cv2.MORPH_CROSS , (3, 3))
    diff =  cv2.morphologyEx(diff , cv2.MORPH_OPEN , k)

    diff_cnt = cv2.countNonZero(diff)

    return diff , diff_cnt


# 카메라 기본 틀
# 움직임 발생시 화면 캡쳐
cap = cv2.VideoCapture(0) # 번호 0부터 +1
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 넓이와 높이 수동 변환
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./fonts/NanumGothicBold.ttf', 20)
# 영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') #H263
is_record = False # 녹화상태

threshold = 40 # 영상 차이가 나는 threshold 설정
diff_max = 10 # 영상 차이가 나는 최대픽셀수

# 초기프레임으로 사용할 프레임 최초 저장
ret , frame_a = cap.read()
ret , frame_b = cap.read()

# 무한루프 (q를 입력할때까지)
while True:
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') # 파일이름에 :이 못들어가기때문 -> 20210720_164728
    
    # 현재영상 입력
    ret , frame = cap.read() # 카메라 현재 영상 로드 , frame에 저장 , ret True/False
    h , w , _ = frame.shape # h, c가 필요없을 때는

    if ret != True:break # ret이 false면 루프 탈출

    # 현재영상과 초기영상 비교 , 움직임 감지
    diff, diff_cnt = get_diff_image(frame_a= frame_a , frame_b= frame_b, frame_c=frame , threshold=threshold)
    print(diff_cnt)
    # 차이나는 이미지갯수가 10개 이상이 나면 움직임이 발생했다고 판단
    if diff_cnt > diff_max :
        cv2.imwrite('./Capture/img_{0}.png'.format(fileDateTime), frame)
        print('움직임 발생 이미지캡쳐 완료')

    # 움직임 결과 영상 출력
    cv2.imshow('Diff Result', diff)

    frame_a = np.array(frame_b) # 이전화면 이전
    frame_b = np.array(frame) # 현재화면 이전
    
    frame = Image.fromarray(frame) # 글자출력을 위해 변환
    draw = ImageDraw.Draw(frame) # 
    draw.text(xy=(10, (h - 40)) , text='실시간 웹캠 - {0}'.format(currDateTime) , font=font, fill=(0,0, 255))
    frame = np.array(frame) # 변환한 거 원상태로 복귀
    
    key = cv2.waitKey(1)
    if key == ord('q') : break # q를 입력하면 루프탈출

    cv2.imshow('RealTime CAM', frame) # 로드한 영상을 창에 띄움

cap.release() # 웹캠 해제
cv2.destroyAllWindows()