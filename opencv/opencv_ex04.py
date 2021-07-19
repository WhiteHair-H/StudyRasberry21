import cv2
import numpy as np

org = cv2.imread('./image/Cat.jpg', cv2.IMREAD_GRAYSCALE) # 이미지 로드
dst = cv2.resize(org, dsize=(640, 480))

center= (250 , 250)
color = ( 0 , 0 ,255)

cv2.rectangle(dst , (100, 100), (500, 300) , (255, 0 , 0)) # 사각형
cv2.circle(dst, center , 30 , color) # 원

cv2.imshow("dest" , dst) #이미지 창띄우기

cv2.waitKey(0) # 키 대기
cv2.destroyAllWindows() # openCV  인스턴스 종료