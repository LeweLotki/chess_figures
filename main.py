import cv2 
import numpy as np 
import random
from mypackages import fun2 as fun

points = []
ratio_list = []
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if (cap.isOpened()== False):  
  print("Error opening video  file")
ret, frame = cap.read()  
n =  10*int((frame.shape[0]*frame.shape[1])**0.5)
while(cap.isOpened()): 
    points.clear()
    m = 0
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    while m < n:
        x = random.randint(0, frame.shape[0]-1)
        y = random.randint(0, frame.shape[1]-1)
        points.extend([[x,y]])
        m += 1
    # frame_contrast = fun.contrast(frame_gray)
    fun.detection_gray(points, frame_gray) 
    if len(points) > 5:
        ave_gray = fun.average_gray(points, frame_gray)
        max_height, min_height, max_width, min_width = fun.extremum(points)
        # print(max_height, min_height, max_width, min_width)
        height = max_height - min_height
        width = max_width - min_width
        ratio = height / width
        ratio_list.append(ratio)
        # print(ratio)
        if ratio > 3 and ave_gray > 50:
            print("white king")
        elif ratio > 3 and ave_gray < 50:
            print("black king")
        elif ratio > 2.7 and ratio < 3 and ave_gray > 50:
            print("white queen")
        elif ratio > 2.7 and ratio < 3 and ave_gray < 50:
            print("black queen")
        elif ratio > 2.4 and ratio < 2.7 and ave_gray > 50:
            print("white bishop")
        elif ratio > 2.4 and ratio < 2.7 and ave_gray < 50:
            print("black bishop")
        elif ratio > 2.2 and ratio < 2.4 and ave_gray > 50:
            print("white rook")
        elif ratio > 2.2 and ratio < 2.4 and ave_gray < 50:
            print("black rook")
        elif ratio > 2 and ratio < 2.2 and ave_gray > 50:
            print("white knight")
        elif ratio > 2 and ratio < 2.2 and ave_gray < 50:
            print("black knight")
        elif ratio < 1.5 and ave_gray > 50:
            print("white pawn")
        elif ratio < 1.5 and ave_gray < 50:
            print("black pawn")
    if ret == True: 
        cv2.imshow('Frame', frame_gray) 
        # cv2.imshow('Contrast', frame_contrast)
    
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break

    elif cv2.waitKey(25) & 0xFF == ord('c'): 
        avg = fun.average2(ratio_list)
        dev = fun.deviation(ratio_list, avg)
        print(avg, dev)
        
cap.release() 
cv2.destroyAllWindows() 
