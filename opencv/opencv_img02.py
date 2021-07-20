import cv2
import numpy as np

org = cv2.imread('./image/Cat.jpg',cv2.IMREAD_REDUCED_COLOR_2)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h , w ,c = org.shape
print('Width:{0}, Height:{1} , Channel:{2}'.format(w, h ,c))

size_small = cv2.resize(gray , dsize=(int(w / 2),int( h / 2)))

cv2.imshow('Original', org) #cv2 새창 열림
cv2.imshow('Gray', gray)
cv2.imshow('Resize', size_small)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() # 메모리 해제



