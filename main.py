import pyautogui
import math
import time

SPEED = 90
RADIUS = 400
Y_OFFSET = 51.8
X_OFFSET = 0

def getX(t, rad):
    return ((pyautogui.size()[0] / 2) + math.cos(t) * rad) + X_OFFSET

def getY(t, rad):
    return ((pyautogui.size()[1] / 2) + math.sin(t) * rad) + Y_OFFSET

for i in range(5):
    print(str(5 - i) + '!')
    time.sleep(0.5)

pyautogui.moveTo(getX(0, RADIUS), getY(0, RADIUS))
pyautogui.mouseDown(button="left")
for i in range(SPEED + 2):
    t = i * math.pi / (SPEED / 2)
    pyautogui.moveTo(getX(t, RADIUS), getY(t, RADIUS), duration=0)
pyautogui.mouseUp(button='left')
