#importing all the necessary modules
import cv2
import numpy as np
from matplotlib import pyplot as plt

#reading image and image preprocessing
img = cv2.imread('C://Users//asus//Downloads//pothole.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image',img)
cv2.imshow('Gray image',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)

    return resized


#Contour detection
ret,thresh = cv2.threshold(gray,127,255,0)
image1, contours1, hierarchy1 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

plt.imshow(image1, cmap=plt.cm.Greys_r)
plt.show()
image2, contours2, hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

plt.imshow(image2, cmap=plt.cm.Greys_r)
plt.show()

#img2 = im.copy()

#plt.imshow(img2, cmap=plt.cm.Greys_r)
#plt.show()

out = cv2.drawContours(gray, contours2, -1, (0,250,0),1)
plt.imshow(out)
plt.show()


#Erosion and dilation
kernel = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations = 1)
cv2.imshow('Eroded', img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

img_dilation = cv2.dilate(img_erosion, kernel, iterations = 3)
cv2.imshow('dilated', img_dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()


#Canny edge detection
edges = cv2.Canny(img_dilation, 300, 300)
plt.subplot(121)
plt.imshow(edges, cmap = 'gray')
