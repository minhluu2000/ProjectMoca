import cv2 as cv
import pyautogui as auto

# Load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

# Capture from webcam
cap = cv.VideoCapture(0)


# Rescale function
def rescale_frame(fr, percent=150):
    w = int(fr.shape[1] * percent / 100)
    h = int(fr.shape[0] * percent / 100)
    dim = (w, h)
    return cv.resize(fr, dim, interpolation=cv.INTER_AREA)


def mm_norm(x, y):
    """A min-max normalization function that transforms the original x and y into the intervals [5, 1920]
    and [5, 1080] respectively"""
    min_x = 0
    new_x_min = 5
    max_x = 515
    new_x_max = 1920

    min_y = 0
    new_y_min = 5
    max_y = 320
    new_y_max = 1080
    x_norm = (((x - min_x) * (new_x_max - new_x_min)) / (max_x - min_x)) + new_x_min
    y_norm = (((y - min_y) * (new_y_max - new_y_min)) / (max_y - min_y)) + new_y_min
    return x_norm, y_norm


while True:
    # Read the frame
    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    # frame150 = rescale_frame(frame, 150)

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

        col_norm, row_norm = mm_norm(column, row)
        auto.moveTo(col_norm, row_norm)

    cv.imshow('video', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
