
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import pandas as pd
import cv2
import time

# DVCT1
VIDP1 = 'C:\\Users\\sturr\\OneDrive\\Desktop\\DVCT1.mp4'
cap = cv2.VideoCapture(VIDP1)
if not cap.isOpened():
    print("File Corrupt or Could not be opened")
    exit()
TTD = 0
FC = 0
MDT = 20
SDT = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.createBackgroundSubtractorMOG2().apply(gray)
    threshold = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    TD = len(contours)
    TTD += TD
    FC += 1
    cv2.putText(frame, f'Traffic Density: {TD}', (10, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Traffic Density", frame)
    current_time = time.time()
    elapsed_time = current_time - SDT
    if elapsed_time >= MDT:
        break
    if cv2.waitKey(100) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
TDN = round(round(TTD / FC) / 10 - 3)
print(f"Traffic Density for Video 1 North Side: {TDN}")


# DVCT2
video_path = 'C:\\Users\\sturr\\OneDrive\\Desktop\\DVCT2.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
TTD = 0
FC = 0
MDT = 25
SDT = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.createBackgroundSubtractorMOG2().apply(gray)
    threshold = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)[1]
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    TD = len(contours)
    TTD += TD
    FC += 1
    cv2.putText(frame, f'Traffic Density: {TD}', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Traffic Density", frame)
    current_time = time.time()
    elapsed_time = current_time - SDT
    if elapsed_time >= MDT:
        break
    if cv2.waitKey(100) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
TDS = round(round(TTD / FC) / 10)
print(f"Traffic Density for Video 2 South Side: {TDS}")
tdn = TDN
tds = TDS
wtn = wts = rtn = rts = 30
if tdn >= 8:
    if tds <= 2:
        wts += 15
        wtn -= 15
        rtn += 15
        rts -= 15
    elif tds <= 5:
        wts += 8
        wtn -= 8
        rtn += 8
        rts -= 8
    elif tds < 8:
        wts += 3
        wtn -= 3
        rtn += 3
        rts -= 3
    elif tds >= 8:
        wts = wtn = rtn = rts = 30
elif tdn >= 6:
    if tds <= 2:
        wts += 10
        wtn -= 10
        rtn += 10
        rts -= 10
    elif tds <= 5:
        wts += 5
        wtn -= 5
        rtn += 5
        rts -= 5
    elif 5 <= tds < 8:
        wts = wtn = rtn = rts = 30
    elif tds >= 8:
        wtn += 5
        wts -= 5
        rts += 5
        rtn -= 5
elif tdn >= 4:
    if tds <= 2:
        wts += 7
        wtn -= 7
        rtn += 7
        rts -= 7
    elif tds <= 5:
        wts = wtn = rtn = rts = 30
    elif 5 <= tds < 8:
        wtn += 5
        wts -= 5
        rts += 5
        rtn -= 5
    elif tds >= 8:
        wtn += 10
        wts -= 10
        rts += 10
        rtn -= 10
elif tdn >= 2:
    if tds >= 8:
        wtn += 12
        wts -= 12
        rts += 12
        rtn -= 12
    elif tds >= 5:
        wtn += 8
        wts -= 8
        rts += 8
        rtn -= 8
    elif tds >= 2:
        wts = wtn = rtn = rts = 30
    elif tds < 2:
        wts += 3
        wtn -= 3
        rtn += 3
        rts -= 3
elif tdn < 2:
    if tds >= 8:
        wtn += 15
        wts -= 15
        rts += 15
        rtn -= 15
    elif tds >= 5:
        wtn += 10
        wts -= 10
        rts += 10
        rtn -= 10
    elif tds >= 2:
        wtn += 3
        wts -= 3
        rts += 3
        rtn -= 3
    elif tds < 2:
        wts = wtn = rtn = rts = 30

print('Traffic North:', tdn)
print('Traffic South:', tds)
print('Stop Time North:', wtn)
print('Stop Time South:', wts)
print('Go Time North:', rtn)
print('Go Time South:', rts)



from tkinter import*
mas=Tk()
mas.geometry("420x420")
Sho= Label(mas, text="Go time for South"+str(rts)+ "seconds",font=(50))
Sho.pack()
Nho= Label(mas, text="Go time for North"+str(rtn)+ "seconds",font=(50))
Nho.pack()
mas.mainloop()