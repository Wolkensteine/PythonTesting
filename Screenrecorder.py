#! /usr/bin/env python3
# all those imports following must be installed on your system
import cv2
import numpy as np
import pyautogui
import time

print("please enter a number of seconds to record!")

recordTime = input()

print("please enter a framerate")

frameRate = input()

screen = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("output.mp4", fourcc, int(frameRate), screen)

print("It will be recorded for: " + recordTime + " seconds")

for i in range(int(frameRate)*int(recordTime)):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    print(i)
    sleep = 1 / int(frameRate)
    time.sleep(sleep)

output.release()
print("Done!")
