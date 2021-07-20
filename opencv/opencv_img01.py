import cv2
import numpy as np

org = cv2.imread('./image/Cat.jpg')

cv2.imshow('Original', org) #cv2 새창 열림

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제



