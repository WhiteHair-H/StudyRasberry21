import cv2
import numpy as np

# 이미지 로드 기본틀
## 이미지 대비
org = cv2.imread('./image/Cat.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org , cv2.COLOR_BGR2GRAY)
enhanced = cv2.equalizeHist(gray)

cv2.imshow('Original', org) #cv2 새창 열림
cv2.imshow('Enhance', enhanced) #cv2 새창 열림

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제



