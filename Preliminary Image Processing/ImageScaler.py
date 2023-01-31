# Python code to read image
import cv2

cv2.namedWindow("output", cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions
 
# To read image from disk, we use cv2.imread function, in below method,
img = cv2.imread("veinImage1.jpg", cv2.IMREAD_COLOR)
 
imS = cv2.resize(img, (1080, 200))                # Resize image
gray1 = cv2.normalize(imS, imS, -200, 200, cv2.NORM_MINMAX) # Edit image contrast and brightness
cv2.imshow("output", gray1)                       # Show image

cv2.waitKey(0)
cv2.destroyAllWindows()



