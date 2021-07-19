
import cv2 as cv
from imutils.video import FPS

camera = cv.VideoCapture(0)
# Make sure you installed opencv-contrib-python, not regular opencv-python for this to work
tracker = cv.TrackerKCF_create()

fps = None
b_box = None

# Video Loop
while True:
    ret, frame = camera.read()

    if ret:
        # Flip the camera feed horizontally
        frame = cv.flip( frame, 1)

        # If user previously selected an object to track
        if b_box is not None:
            # Update the bounding box, update the location of tracked object
            success, b_box = tracker.update( frame )
            fps.update()
            fps.stop()

            # Tracked. Draw the rectangle around the object tracked
            if success:
                x, y, w, h = b_box
                cv.rectangle( frame, ( int(x), int(y) ), ( int(x+w), int(y+h) ), (0,0,0,0), 2, 1  )
                cv.putText( frame, f'{ int(fps.fps() )}', (0,10), cv.FONT_HERSHEY_COMPLEX, .5, (0,0,0), 1  )

        # Show the camera frame
        cv.imshow('Camera', frame)

        # Wait for input
        key_input = cv.waitKey(33) & 0xff

        # If user pressed 'q', quit program
        if key_input == ord('q'):
            break
        # If user pressed 's', allow user to select an object to be tracked
        elif key_input == ord('s'):
            # Text prompt
            cv.putText(frame, 'Click and drag to select, Enter or spacebar to confirm', (0,15),
                       cv.FONT_HERSHEY_COMPLEX, .5, (0,0,0) )
            # Select Area of Interest (Object to Track)
            b_box = cv.selectROI('Camera', frame, fromCenter=False, showCrosshair=True)

            # Create an object tracker around the selected area
            tracker = cv.TrackerKCF_create()
            tracker.init( frame, b_box )
            fps = FPS().start()


camera.release()
cv.destroyAllWindows()