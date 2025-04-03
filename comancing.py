import numpy as np

print(type((500//3, 400)))
width, height = 500, 550
img = np.full((height, width, 3), 200, np.uint8)
title = "button_play"
pt1, pt2 = (int(width//3), height-150), (int(width//1.5), height) 
print(pt1, pt2)