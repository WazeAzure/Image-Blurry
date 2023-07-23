import cv2 as cv

img = cv.imread('img.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imwrite('img_rgb.jpg', img_rgb)
