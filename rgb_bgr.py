import cv2 as cv

img = cv.imread('img.jpg')

print(img.shape)

# format opencv - BGR
counter = 60000;
current = 0;

for a in range(0, 3000):
    for b in range(0, 1000):
        for x in range(0, 3):
            img[a][b][x] = 255-img[a][b][x]
        current = current + 1;
        print(current)

cv.imwrite('result.jpg', img)
