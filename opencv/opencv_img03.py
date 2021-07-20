import cv2
import numpy as np

# 이미지 로드 기본틀
org = cv2.imread('./image/Cat.jpg', cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w , c = org.shape

cropped = gray[:, :int(w/2)] # 이미지 넓이를 반으로 자르기(회색)
cropped = gray[:int(h/2), :] # 이미지 높이를 반으로 자르기(회색)


cv2.imshow('Original', org) #cv2 새창 열림
cv2.imshow('Cropped' , cropped) # 반으로 자른 이미지


cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제



