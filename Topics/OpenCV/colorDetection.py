import cv2 as cv
import numpy as np


#############################################
#   SLIDERS WINDOW - Menu for sliders control
#############################################
hue = 0
hueTolerance = 0
saturationLow = 0
saturationHigh = 0
valueLow = 0
valueHigh = 0

detectionArea = 300

def hueOnChange(val):
    global hue
    hue = val
def hueToleranceOnChange(val):
    global hueTolerance
    hueTolerance = val
def saturationLowOnChange(val):
    global saturationLow
    saturationLow = val
def saturationHighOnChange(val):
    global saturationHigh
    saturationHigh = val
def valueLowOnChange(val):
    global valueLow
    valueLow = val
def valueHighOnChange(val):
    global valueHigh
    valueHigh = val
def detectionAreaOnChange(val):
    global detectionArea
    detectionArea = val


cv.namedWindow('My Slider', cv.WINDOW_NORMAL)
cv.createTrackbar('Hue', 'My Slider', 0, 180, hueOnChange)
cv.createTrackbar('Hue Tolerance', 'My Slider', 0, 180, hueToleranceOnChange)
cv.createTrackbar('Saturation', 'My Slider', 0, 255, saturationLowOnChange)
cv.createTrackbar('Saturation Tolerance', 'My Slider', 0, 255, saturationHighOnChange)
cv.createTrackbar('Value', 'My Slider', 0, 255, valueLowOnChange)
cv.createTrackbar('Value Tolerance', 'My Slider', 0, 255, valueHighOnChange)
cv.createTrackbar('Detection Area', 'My Slider', 300, 2000, detectionAreaOnChange)



###########################################
#   RED COLOR DETECTOR
###########################################
def redDetection(hsvFrame, frame):
    low = np.array([ 160, 100, 100] )
    high = np.array([ 200, 255 , 255] )

    mask = cv.inRange( hsvFrame, low, high )

    cv.imshow('Red Masked', cv.bitwise_and(frame, frame, mask=mask) )

    contours, hierarchy = cv.findContours( mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )

    for pic, contour in enumerate( contours ):
        if cv.contourArea( contour ) > detectionArea:
            x,y,w,h = cv.boundingRect( contour )
            cv.rectangle( frame, (x,y), (x+w, y+h), (0,0,255), 2)
            cv.putText( frame, 'Red', (x, y-10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255) )


###########################################
#   BLACK DETECTOR
###########################################
def blackDetection(hsvFrame, frame):
    low = np.array([ 0, 0, 0] )
    high = np.array([ 180, 255 , 40] )

    mask = cv.inRange( hsvFrame, low, high )

    contours, hierarchy = cv.findContours( mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )

    for pic, contour in enumerate( contours ):
        if cv.contourArea( contour ) > detectionArea:
            x,y,w,h = cv.boundingRect( contour )
            cv.rectangle( frame, (x,y), (x+w, y+h), (0,0,0), 2)
            cv.putText( frame, 'Black', (x, y-10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0) )


###########################################
#   MAIN LOOP
###########################################
camera = cv.VideoCapture(0)

while camera.isOpened():
    _, frame = camera.read()
    frame = cv.flip(frame, 1)

    hsvFrame = cv.cvtColor( frame, cv.COLOR_BGR2HSV )
    low = np.array([ hue - hueTolerance, saturationLow, valueLow ] )
    high = np.array([ hue + hueTolerance, saturationHigh, valueHigh ] )

    mask = cv.inRange(hsvFrame, low, high)

    redDetection(hsvFrame, frame)
    blackDetection(hsvFrame, frame)


    cv.imshow('Capture', frame)
    cv.imshow('Masked', mask)

    if cv.waitKey(30) == ord('e'):
        break



camera.release()
cv.destroyAllWindows()