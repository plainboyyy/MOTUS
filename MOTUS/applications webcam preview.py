import cv2
import time
import datetime
import imutils
import PyPDF2

import tkinter as tk
import mediapipe as mp

from tkinter import *
from PIL import Image
from PIL import ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3)

label =Label(root)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)



def preview():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, preview)

preview()
instructions = tk.Label(root, text="Welcome to MOTUS", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

btn_txt = tk.StringVar()
btn = tk.Button(root, textvariable=btn_txt, command=lambda:motion_capture(), font="Raleway")
btn_txt.set("Start Motion")
btn.grid(column=1, row=2)

s_txt = tk.StringVar()
s_btn = tk.Button(root, textvariable=s_txt, command=lambda:settings(), font="Raleway")
s_txt.set("Settings tab")
s_btn.grid(column=3, row=0)


root.mainloop()
