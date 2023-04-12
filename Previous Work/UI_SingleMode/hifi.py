import cv2
import numpy as np

THIN_VEIN_THRESHOLD = 50
MEDIUM_VEIN_THRESHOLD = 100


def enhance_contrast(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(gray)
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    return img_output

def process_frame(frame):
    contrast_enhanced = enhance_contrast(frame)
    gray = cv2.cvtColor(contrast_enhanced, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, THIN_VEIN_THRESHOLD, 255, cv2.THRESH_BINARY_INV)

    contours,_ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area < MEDIUM_VEIN_THRESHOLD:
            cv2.drawContours(frame, [c], -1, (0, 0, 255), 2)
        elif area < THIN_VEIN_THRESHOLD:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        else:
            cv2.drawContours(frame, [c], -1, (255, 0, 0), 2)

    return frame

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = process_frame(frame)
        cv2.imshow('Vein Detection', processed_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


main()
