import mediapipe as mp
import cv2
import time

capture_video = cv2.VideoCapture(0)

if __name__ == "__main__":
    while True:
        success, img = capture_video.read()
        cv2.imShow("Image", img)
        cv2.waitkey(1)