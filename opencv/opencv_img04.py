import cv2
import numpy as np

# 이미지 로드 기본틀
## 이미지 흐리게 하기
org = cv2.imread('./image/Cat.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY) # 회색 이미지
blur = cv2.blur(org , (10, 10))
kernel = np.array([[ 0, -1 ,0], [ -1 , 5 ,-1] , [0 , -1 ,0]])
sharp = cv2.filter2D(org, -1, kernel)

cv2.imshow('Original', org) #cv2 새창 열림
cv2.imshow('blur', blur) #cv2 새창 열림
cv2.imshow('Sharp', sharp) #cv2 새창 열림

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제



