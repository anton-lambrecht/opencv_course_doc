import cv2 as cv

#load an image
#img = cv.imread('test.jpg')
#cv.imshow('test', img)
#cv.waitKey(0)

#load a video
capture = cv.VideoCapture(0)#0 voor webcam

#capture = cv.VideoCapture('testV.mov')
while True:
    isTrue, frame = capture.read() #isTrue is boolean die aanduid of goed ingelezen is
    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'): #de tweede is als je op d drukt dat eruit wordt gebroken
        break

capture.release()
cv.destroyAllWindows()

