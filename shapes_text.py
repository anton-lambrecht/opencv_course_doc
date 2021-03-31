import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') #height, width en dan aantal kleurenkanalen
cv.imshow('blank', blank)

blank[:] = 0,250,0
cv.imshow('green', blank)

blank[200:300, 200:300] = 0,0,250
cv.imshow('square', blank)

#voor een rechthoek
#cv.rectangle(blank, (0,0), (250, 250), (250, 250, 250), thickness = 2) #thickness = cv.FILLED dit vult de rechthoek
#cv.imshow('rectangle', blank)

#voor een cirkel
#cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (250, 250, 250), thickness = 2) #thickness = cv.FILLED dit vult de rechthoek
#cv.imshow('circle', blank)

#voor een lijn
#cv.line(blank, (0,0), (30, 200), (89, 67, 56), thickness=3)
#cv.imshow('line', blank)

#voor text
cv.putText(blank, "hallo", (20, 30), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0, 0), thickness=4)
cv.imshow('text', blank)


cv.waitKey(0)
