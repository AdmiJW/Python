
import cv2 as cv
from imutils.video import FPS

camera = cv.VideoCapture(0)
tracker = cv.TrackerKCF_create()

fps = None
b_box = None

# Video Loop
while True:
    ret, frame = camera.read()

    if ret:
        frame = cv.flip( frame, 1)

        if b_box is not None:
            success, b_box = tracker.update( frame )
            fps.update()
            fps.stop()

            if success:
                x, y, w, h = b_box
                cv.rectangle( frame, ( int(x), int(y) ), ( int(x+w), int(y+h) ), (0,0,0,0), 2, 1  )
                cv.putText( frame, f'{ int(fps.fps() )}', (0,10), cv.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 1  )


        cv.imshow('Camera', frame)

        key_input = cv.waitKey(33) & 0xff

        if key_input == ord('q'):
            break
        elif key_input == ord('s'):
            cv.putText(frame, 'Click and drag to select, Enter or spacebar to confirm', (0,15),
                       cv.FONT_HERSHEY_COMPLEX, .5, (0,0,0) )
            b_box = cv.selectROI('Camera', frame, fromCenter=False, showCrosshair=True)
            tracker = cv.TrackerKCF_create()
            tracker.init( frame, b_box )
            fps = FPS().start()


camera.release()
cv.destroyAllWindows()