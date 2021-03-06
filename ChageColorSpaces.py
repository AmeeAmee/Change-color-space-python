import cv2
import  numpy as np

img = cv2.imread('HappyFish.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('happyfish', img)
cv2.imshow('grayscale', img2)
cv2.imshow('yuv', img3)
cv2.imshow('hsv', img4)

cv2.imshow('y channel', img3[:, :, 0])
cv2.imshow('u channel', img3[:, :, 1])
cv2.imshow('v channel', img3[:, :, 2])


cv2.waitKey()
