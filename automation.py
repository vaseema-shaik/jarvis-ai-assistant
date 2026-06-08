import webbrowser
import os
import cv2

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_github():
    webbrowser.open("https://github.com")

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

def open_cmd():
    os.system("start cmd")

def open_paint():
    os.system("mspaint")

def open_camera():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not found")
        return

    print("Press Q to close camera")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()