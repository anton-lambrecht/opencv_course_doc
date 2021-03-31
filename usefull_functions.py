import cv2 as cv
import numpy as np

img = cv.imread('test2.JPG')

cv.imshow('test', img)

#convert to greyscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('grey', gray)

#blur an image
#blur  = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
#cv.imshow('blur', blur)

#edge cascade
#canny = cv.Canny(img, 125, 175)
#cv.imshow('canny', canny)#als je te veel edges hebbt kan je ze eerst blurren en dan pas de edges zoeken

#dialating the image
#dilated = cv.dilate(canny, (3, 3), iterations=1)
#cv.imshow('dilated', dilated)

#eroding the image(omgekeerde van dilated)
#eroded = cv.erode(dilated, (3, 3), iterations=1)
#cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)
#Nearest neighbor will be as fast as possible, but you will lose substantial information when resizing.
#Linear interpolation is less fast, but will not result in information loss unless you're shrinking the image (which you are).
#Cubic interpolation (probably actually "Bicubic") uses one of many possible formulas that incorporate multiple neighbor pixels. This is much better for shrinking images, but you are still limited as to how much shrinking you can do without information loss. Depending on the algorithm, you can probably reduce your images by 50% or 75%. The primary con of this approach is that it is much slower.
#Not sure what "area" is - it may actually be "Bicubic". In all likelihood, this setting will give your best result (in terms of information loss / appearance), but at the cost of the longest processing time.

#cropping
cropped = img[200:300, 100:300]
cv.imshow('cropped', cropped)

cv.waitKey(0)