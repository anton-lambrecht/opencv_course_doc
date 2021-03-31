import cv2 as cv

#dit kan met alles
def rescaleFrame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

#dit kan enkel met live videos dus ook niet met video files
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)#nummers representerenn gwn de properties je hebt er ook bv 1 voor de brightness


img = cv.imread('test.jpg')
cv.imshow('test', img)
cv.imshow('test_resize', rescaleFrame(img, 0.60))


capture = cv.VideoCapture('testV.mov')
while True:
    isTrue, frame = capture.read() #isTrue is boolean die aanduid of goed ingelezen is
    frame_resized = rescaleFrame(frame, 0.75)

    cv.imshow('video', frame)
    cv.imshow('video_resize', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): #de tweede is als je op d drukt dat eruit wordt gebroken
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)