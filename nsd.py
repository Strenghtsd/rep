import cv2, time
import numpy as np
import sys as s

"""
def onMouse(event, x, y, flag, param=None):
    global img, title, key, width, height
    if event == cv2.EVENT_LBUTTONDOWN and y > 400:
        if x < (width//3):
            print("left")
        elif (width//3) <= x < (width//1.5) and y < (height + 75):
            print("up")
        elif (width//3) <= x < (width//1.5) and y >= (height + 75):
            print("down")
        else:
            print("right")
"""

flag = False

class Event:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def make3dim(self, title):
        self.img = np.full((self.height, self.width, 3), 211, np.uint8)
        self.title = title
        self.b, self.g, self.r = 0, 0, 0
        
    def onMouse(self, event, x, y, flag, param=None):
        if event == cv2.EVENT_LBUTTONDOWN and y > 400:
            if x < (self.width//3):
                self.b = self.value
                self.img[:400][:400][:400] = (self.b, self.g, self.r)
                cv2.rectangle(self.img, (20, 425, 130, 100), (211, 211, 211), -1)
                cv2.putText(self.img, str(self.b), (self.width//6-50, 400+(self.height-400)//2), 1, 3.0, (self.b, 0, 0), 1)
                cv2.imshow(self.title, self.img)
                
            elif (self.width//3) <= x <(self.width//1.5):
                self.g = self.value
                self.img[:400][:400][:400] = (self.b, self.g, self.r)
                cv2.rectangle(self.img, (170, 425, 150, 100), (211, 211, 211), -1)
                cv2.putText(self.img, str(self.g), (self.width//2-50, 400+(self.height-400)//2), 1, 3.0, (0, self.g, 0), 1)
                cv2.imshow(self.title, self.img)
                
            else:
                self.r = self.value
                self.img[:400][:400][:400] = (self.b, self.g, self.r)
                cv2.rectangle(self.img, (380, 425, 90, 80), (211, 211, 211), -1)
                cv2.putText(self.img, str(self.r), (self.width-125, 400+(self.height-400)//2), 1, 3.0, (0, 0, self.r), 1)
                cv2.imshow(self.title, self.img)
                
            
    def onChange(self, value):
        self.img[:400][:400][:400] = value
        self.value = value
    
    def reSizing(self, width, height):
        self.img = cv2.resizeWindow(self.title, width, height)
        self.height = height
        self.width = width
    
    def makeRect(self, pt1, pt2, color):
        cv2.rectangle(self.img, pt1, pt2, color, 3, cv2.LINE_4)


if __name__ == "__main__":
    e = Event(500, 550)
    e.make3dim("Button_play")
    #cv2.rectangle(e.img, (0, e.height-150), (int(e.width//3), e.height), (180, 70, 0), 3, cv2.LINE_8)
    #cv2.rectangle(e.img, (int(e.width//3), e.height-150), (int(e.width//1.5), e.height), (0, 180, 70), 3, cv2.LINE_8)
    #cv2.rectangle(e.img, (int(e.width//1.5), e.height-150), (e.width, e.height), (70, 0, 180), 3, cv2.LINE_8)
    e.makeRect((0, e.height-150), (int(e.width//3), e.height), (180, 70, 0))
    e.makeRect((int(e.width//3), e.height-150), (int(e.width//1.5), e.height), (0, 180, 70))
    e.makeRect((int(e.width//1.5), e.height-150), (e.width, e.height), (70, 0, 180))

    cv2.imshow(e.title, e.img)
    cv2.setMouseCallback(e.title, e.onMouse)
    cv2.createTrackbar("Brightness", e.title, e.img[0][0][0], 255, e.onChange)

    while True: 
        key = cv2.waitKeyEx(0)
        if key == 27: break
        elif cv2.getWindowProperty(e.title, cv2.WND_PROP_VISIBLE) < 1: flag = True ; break

    if flag == True: s.exit(0)
    cv2.destroyWindow(e.title)


    """
    def onMouse(event, x, y, flag, param=None):
        global width
        if event == cv2.EVENT_LBUTTONDOWN and y > 400:
            if x < (width//3):
                print("blue part")
            elif (width//3) <= x <(width//1.5):
                print("green part")
            else:
                print("red part")

    def onChange(value):
        global img, title

        img[:398][:][:] = value
        cv2.imshow(title, img)

    width, height = 500, 550
    img = np.full((height, width, 3), 200, np.uint8)
    title = "button_play"

    cv2.rectangle(img, (0, height-150), (int(width//3), height), (180, 70, 0), 3, cv2.LINE_8)
    cv2.rectangle(img, (int(width//3), height-150), (int(width//1.5), height), (0, 180, 70), 3, cv2.LINE_8)
    cv2.rectangle(img, (int(width//1.5), height-150), (width, height), (70, 0, 180), 3, cv2.LINE_8)
    cv2.imshow(title, img)
    cv2.createTrackbar("Brightness", title, img[0][0][0], 255, onChange)
    cv2.setMouseCallback(title, onMouse)

    while True:
        key = cv2.waitKeyEx(0)
        if key == 27: break

    cv2.destroyWindow(title)
    """