import numpy as np
import cv2 as cv
import pyautogui as auto

# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Capture from webcam
cap = cv.VideoCapture(0)

# Rescale function
def rescale_frame(fr, percent=150):
    w = int(fr.shape[1] * percent / 100)
    h = int(fr.shape[0] * percent / 100)
    dim = (w, h)
    return cv.resize(fr, dim, interpolation=cv.INTER_AREA)


while True:
    # Read the frame
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    frame150 = rescale_frame(frame, 150)

    # Convert to grayscale
    gray = cv.cvtColor(frame150, cv.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (column, row, width, height) in faces:
        cv.rectangle(
            frame150,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )
        auto.moveTo(column, row)

    cv.imshow('video', frame150)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()