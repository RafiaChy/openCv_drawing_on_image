import cv2

img = cv2.imread('baboon.jpg', 1)
# # cv2.line(img, (0,255),(400,255), (0,255,255), 10)
# cv2.rectangle(img,(0,0),(400,400), (0,0,255), 5)

# # cv2.rectangle(img,(0,0),(400,400), (0,0,255), -1)
# cv2.circle(img, (255,255), 40, (255, 0, 0), 5)

cv2.circle(img, (255,255), 40, (255, 0, 0), -1)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()