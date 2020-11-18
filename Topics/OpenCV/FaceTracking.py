
import cv2 as cv
import keras

face_class = cv.CascadeClassifier('frontalface.xml')

camera = cv.VideoCapture(0)

while True:
    read, frame = camera.read()

    if read:
        frame = cv.flip(frame, 1)

        grey_scaled = cv.cvtColor( frame, cv.COLOR_BGR2GRAY )
        faces = face_class.detectMultiScale( grey_scaled, 1.1, 8 )

        for x,y,w,h in faces:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,0), 2)

        cv.imshow('Camera', frame)

        key_input = cv.waitKey(34) & 0xff
        if key_input == ord('q'):
            break
    else:
        break

camera.release()
cv.destroyAllWindows()