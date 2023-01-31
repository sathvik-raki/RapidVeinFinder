import numpy as np
import cv2
from matplotlib import pyplot as plt


# reading the video
#source = cv2.VideoCapture(0)
source = cv2.VideoCapture('Video2.avi')


frame_width = int(source.get(3))
frame_height = int(source.get(4))   
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename2.avi',  cv2.VideoWriter_fourcc(*'MJPG'),10, size)

#img = cv2.imread('veinImage1.jpg',0)
#img = img[150:300,150:350]

a = 0
b = 255

while True:
    ret, img = source.read()
    
    if ret == True:
        kernel = np.ones((5,5), np.uint8)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        img = cv2.normalize(img,img, a, b, cv2.NORM_MINMAX)
        
        # create a CLAHE object (Arguments are optional).
        clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(7,7))
        cl1 = clahe.apply(img)

        #apply adaptive threshold
        cl2 = cv2.medianBlur(cl1, 5)
        th1 = cv2.adaptiveThreshold(cl2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,2.55)

        #apply otsu threshold
        blur = cv2.GaussianBlur(cl1,(5,5),0)
        ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        #removing noise 
        th2 = th1 & th3

        #morphological transform
        opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

        #finding outlines via contouring process
        contours, hierarchy = cv2.findContours(opening,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) 
        dst = cv2.drawContours(img1, contours, -1, (0,255,0), -1)
        
        result.write(dst)
        
        cv2.imshow("Live", dst)
        
        key = cv2.waitKey(1)
        if key == ord("q"):
            source.release()
            break
        
    else:
        break
    
#printing the results onto the screen
#cv2.imwrite("out.jpg", dst)
#cv2.imwrite("dst.jpg",dst)
print (a,b)

source.release()
result.release()