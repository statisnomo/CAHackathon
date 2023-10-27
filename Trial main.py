import cv2
import numpy as np
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk


class TrafficDensityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Density")

        self.cap = cv2.VideoCapture(0)
        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.traffic_density_label = tk.Label(root, text="Traffic Density: 0", font=("Helvetica", 16))
        self.traffic_density_label.pack()

        self.update()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            fgmask = cv2.createBackgroundSubtractorMOG2().apply(gray)
            threshold = cv2.threshold(fgmask, 128, 255, cv2.THRESH_BINARY)[1]
            contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            traffic_density = len(contours)
            self.traffic_density_label.config(text=f"Traffic Density: {traffic_density}")

            # Convert the OpenCV frame to a format that can be displayed in tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(image=frame)
            self.video_label.config(image=frame)
            self.video_label.image = frame

        self.root.after(30, self.update)

    def close(self):
        self.cap.release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficDensityApp(root)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()
