import cv2 as cv

img = cv.imread(r'C:\Users\JayaLakshman\opencv\cat.jpg',)
cv.imshow('cat',img)
k = cv.waitKey(0) & 0XFF
print(img.shape)
if k==27:
    cv.destroyAllWindows()
