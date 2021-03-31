import cv2 as cv


img = cv.imread('test2.JPG')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
con = cv.Canny(img, 30, 175)

cv.imshow('image', img)
cv.imshow('cotours', con)

contours, hierarchies = cv.findContours(con, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#cotours is een list van alle contouren
#gebruikt verschillende strategieen
cv.waitKey(0)