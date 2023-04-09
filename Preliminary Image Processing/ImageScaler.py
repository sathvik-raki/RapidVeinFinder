# Python code to read image
import cv2
import numpy as np

cv2.namedWindow("output", cv2.WINDOW_NORMAL)    # Create window with freedom of dimensions
 
# To read image from disk, we use cv2.imread function, in below method,
img = cv2.imread("imageTest2.png", cv2.IMREAD_COLOR)

print(type(img))
 
# imS = cv2.resize(img, (1080, 200))                # Resize image
# gray1 = cv2.normalize(imS, imS, -200, 200, cv2.NORM_MINMAX) # Edit image contrast and brightness
# cv2.imshow("output", gray1)                       # Show image

# cv2.waitKey(0)
# cv2.destroyAllWindows()

contrast = 1
brightness = 5.0
cam_button_press = 0
ClacheClipLimit = 1.2
ClacheTile_one = 7
ClacheTile_two = ClacheTile_one
medianBlur = 5
adaptiveThres_one = 255
adaptiveThres_two = 255
adaptiveThres_three = 7
gaussianBlurTile_one = 5
gaussianBlurTile_two = gaussianBlurTile_one
gaussianBlur = 0
thresh_one = 0
thresh_two = 255

kernel = np.ones((1, 1), np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)

# Create a CLAHE object (Arguments are optional)
clahe = cv2.createCLAHE(clipLimit=ClacheClipLimit, tileGridSize=(ClacheTile_one, ClacheTile_two))
cl1 = clahe.apply(img)

# Apply adaptive threshold
cl2 = cv2.medianBlur(cl1, medianBlur)
th1 = cv2.adaptiveThreshold(cl2, adaptiveThres_one, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, adaptiveThres_two, adaptiveThres_three)

# Apply OTSU threshold
blur = cv2.GaussianBlur(cl1, (gaussianBlurTile_one, gaussianBlurTile_two), gaussianBlur)
ret3, th3 = cv2.threshold(blur, thresh_one, thresh_two, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Removing noise
th2 = th1 & th3

# Morphological transform
opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

# Finding outlines via contouring process
contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
dst = cv2.drawContours(img1, contours, -1, (0, 255, 0), -1)
openingImg = cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR)

cv2.imshow("output", dst)                       # Show image

cv2.waitKey(0)
cv2.destroyAllWindows()


