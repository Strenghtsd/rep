import cv2
import numpy as np
import keyboard as k
import time as t

"""
img = np.full((200, 400), 255, np.uint8)
title = "test"
cv2.imshow(title, img)

while True:
    key = cv2.waitKeyEx(0); print(key)
    if key == 27: break
    
cv2.destroyAllWindows()
"""

"""
flag = False

while True:
    key = k.read_key(); flag = True
    if key == "esc":
        break
    else:
        if flag:
            print(key)
            flag = False
            t.sleep(0.75)     
"""
#------------openCV----------------
def onMouse(event, x, y, flag, param=None):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"L button down, x={x}, y={y}")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"R button down, x={x}, y={y}")


img = np.zeros((200, 400), np.uint8)
img[:] = 255
#img = np.full((200, 400), 200, np.uint8)

title1, title2 = "Position1", "Position2"

switch_case = {ord("a") : "a키"}

cv2.namedWindow(title1, cv2.WINDOW_NORMAL)
cv2.imshow(title1, img)
cv2.resizeWindow(title1, 400, 500)

while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break
    
    try:
        rst = switch_case[key]
        print(rst)
    except KeyError:
        rst = -1

cv2.destroyWindow(title1)

cv2.namedWindow(title2, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title2, img)
cv2.resizeWindow(title2, 400, 500)
cv2.setMouseCallback(title2, onMouse)

while True:
    key = cv2.waitKeyEx(0)
    if key == 27:
        break

cv2.destroyWindow(title2)

def onChange(value):
    global img, title
    
    add_value = value - int(img[0][0])
    print(f"추가 화소값:{add_value}")
    
    img = np.uint8(img + add_value)
    cv2.imshow(title, img)

title = "TrackBar Event"
cv2.imshow(title, img)
cv2.createTrackbar("Brightness", title, img[0][0], 255, onChange)
cv2.waitKeyEx(0)
cv2.destroyWindow(title)

b, g, r = (255, 0, 0), (0, 255, 0), (0, 0, 255)
img = np.full((400, 600, 3), 255, np.uint8)

pt1, pt2 = (50, 50), (250, 350)

cv2.line(img, pt1, pt2, g, 3, cv2.LINE_AA)

cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyWindow("line")


