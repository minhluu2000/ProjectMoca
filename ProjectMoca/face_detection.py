import numpy as np
import cv2 as cv


# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Capture from webcam
cap = cv.VideoCapture(0)

while True:
    # Read the frame
    _, frame = cap.read()

    # Convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (column, row, width, height) in faces:
        cv.rectangle(
            frame,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )

    cv.imshow('video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()