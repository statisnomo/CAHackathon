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




