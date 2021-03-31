import cv2 as cv
import numpy as np

img = cv.imread('test2.JPG')

cv.imshow('test', img)

#translation
def translation(img, x , y):
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

translated = translation(img, 100, 100)
cv.imshow('translated', translated)

#rotation
def rotate(img, angle, rotatepoint=None):
    (height, width) = img.shape[:2]
    if rotate is None:
        rotatepoint = (width//2, height//2)
    rotMatrix = cv.getRotationMatrix2D(rotatepoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

#resizeing
resized = cv.resize(img, (500, 500)) #let op hier ook interpolation kunnen toepassenn
cv.imshow('resized', resized)

#flipping
flipped = cv.flip(img, -1)
cv.imshow('flipped', flipped)


cv.waitKey(0)