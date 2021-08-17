from cv2 import cv2
import win32api, win32con
import ctypes
import socketio
import numpy as np
import time

cam = cv2.VideoCapture(0)
sio = socketio.Client()

@sio.event
def buttonPressed(data):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

@sio.event
def notPressed(data):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

@sio.event
def placePressed(data):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    print('placed')

@sio.event
def notPlace(data):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    print('not placed')

sio.connect('http://ipadress:3000')
print('connected')

while 1:
    try:
        ret, frame = cam.read()
        if not ret:
            print('failed to grab frame')
            break

        frame = cv2.flip(frame, 1)
        
        screenWidth = frame.shape[1]
        screenHeight = frame.shape[0]
        x_medium = int(screenHeight / 2)
        y_medium = int(screenWidth / 2)
        center = int(screenHeight / 2)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 0, 250])
        higher = np.array([0, 0, 255])
        mask = cv2.inRange(hsv, lower, higher)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

        for cnt in contours:
            (x, y, w, h) = cv2.boundingRect(cnt)

            x_medium = int((x + x + w) / 2)
            y_medium = int((y + y + h) / 2)
            break
        
        cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        cv2.line(frame, (0, y_medium), (645, y_medium), (0, 0, 255), 2)

        coords = (x_medium, y_medium)

        ctypes.windll.user32.SetCursorPos(x_medium * 2, y_medium * 2)

        cv2.imshow('frame', frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    except Exception as e:
        print(f'oopsie woopsie i did a doodie. UwU {e}')
        break

cam.release()
cv2.destroyAllWindows()