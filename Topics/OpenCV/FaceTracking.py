
import cv2 as cv

# Make sure to have the frontalface.xml in the same folder
face_classifier = cv.CascadeClassifier('frontalface.xml')

camera = cv.VideoCapture(0)


while True:
    # Read one frame from the camera
    read, frame = camera.read()

    if read:
        # Flips the image, because the camera feed is horizontally flipped
        frame = cv.flip(frame, 1)

        # We'll use grey scaled image (black&white) to feed to the face detection
        grey_scaled = cv.cvtColor( frame, cv.COLOR_BGR2GRAY )
        # Detect faces
        faces = face_classifier.detectMultiScale( grey_scaled, 1.1, 8 )

        # Draw rectangle around face detected
        for x,y,w,h in faces:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,0), 2)

        # Show the output
        cv.imshow('Camera', frame)

        # Wait for 10ms, check if user pressed any key. If key 'q' is pressed, exit program
        key_input = cv.waitKey(10) & 0xff
        if key_input == ord('q'):
            break
    else:
        break

# Release camera feed and destroy all windows
camera.release()
cv.destroyAllWindows()
