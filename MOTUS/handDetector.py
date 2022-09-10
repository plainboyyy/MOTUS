import cv2, time, datetime, imutils, PyPDF2, numpy, uuid, os, wmi, math, pyautogui

import numpy as np
import tkinter as tk
import mediapipe as mp

from tkinter import *
from PIL import Image
from PIL import ImageTk

mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

mp_holistic = mp.solutions.holistic

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
lhd = mp_drawing.DrawingSpec(color=(250, 44, 44), thickness=2, circle_radius=3)
rhd = mp_drawing.DrawingSpec(color=(44, 44, 250), thickness=2, circle_radius=3)

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():

            ret, frame = cap.read()
            start = time.time()

            image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)

            image.flags.writeable = False

            results = hands.process(image)
            hresults = holistic.process(image)
            print(results.multi_hand_landmarks)

            image.flags.writeable = True

            image = cv2.cvtColor(cap.read()[1],cv2.COLOR_RGB2BGR)

            mp_drawing.draw_landmarks(image, hresults.face_landmarks,
                                      mp_holistic.FACEMESH_CONTOURS,
                                      landmark_drawing_spec=drawing_spec,
                                      connection_drawing_spec=drawing_spec)

            mp_drawing.draw_landmarks(image, results.left_hand_landmarks,
                                      mp_holistic.HAND_CONNECTIONS,
                                      landmark_drawing_spec=lhd,
                                      connection_drawing_spec=lhd)

            mp_drawing.draw_landmarks(image, results.right_hand_landmarks,
                                      mp_holistic.HAND_CONNECTIONS,
                                      landmark_drawing_spec=rhd,
                                      connection_drawing_spec=rhd)


            image = cv2.flip(image, 1)
            cv2.imshow("Tracking", image)

            if cv2.waitKey(10) & 0xFF == ord("q"):
                cap.release()
                cv2.destroyAllWindows()