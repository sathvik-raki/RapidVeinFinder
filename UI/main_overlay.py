# Import libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from CapstonePY import Ui_MainWindow

# Define MainWindow class
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Load animation
        self.side_menu = self.ui.side_menu
        self.menu_button = self.ui.menu_button
        self.animation = QPropertyAnimation(self.side_menu, b'geometry')
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        # Initialize webcam and attach video feed to pages
        self.WebCam = WebCam()
        self.WebCam.start()
        self.WebCam.ImageUpdate.connect(self.video_label_slot)

        # Setup landing page
        self.ui.stackedWidget.setCurrentWidget(self.ui.video_page)

        # Auto scale video feed
        self.ui.video_label.setScaledContents(True)

        # Add functionalities to the buttons
        self.ui.video_button.clicked.connect(self.show_video_page)
        self.ui.contrast_button.clicked.connect(self.show_contrast_page)
        self.ui.depth_button.clicked.connect(self.show_depth_page)
        self.ui.info_button.clicked.connect(self.show_info_page)
        self.menu_button.clicked.connect(self.animate_side_menu)

    # Define what will be shown when buttons are clicked
    def show(self):
        self.main_win.show()

    def show_video_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.video_page)

    def show_contrast_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.contrast_page)

    def show_depth_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.depth_page)

    def show_info_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.info_page)

    # Convert video feed to a pixmap
    def video_label_slot(self, Image):
        self.ui.video_label.setPixmap(QPixmap.fromImage(Image))

    # Animation function
    def animate_side_menu(self):
        if self.side_menu.isVisible():
            self.animation.setStartValue(self.side_menu.geometry())
            self.animation.setEndValue(QRect(self.side_menu.x(), self.side_menu.y(), self.side_menu.width(), 0))
            self.side_menu.hide()
        else:
            # If menu bar is hidden, set animation to show it
            self.side_menu.show()
            self.animation.setStartValue(QRect(self.side_menu.x(), self.side_menu.y(), self.side_menu.width(), 0))
            self.animation.setEndValue(self.side_menu.geometry())
        self.animation.start()

# Define webcam class
class WebCam(QThread):

    
    ImageUpdate = pyqtSignal(QImage)

    def run(self):
        self.ThreadActive = True

        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            a = 0
            b = 255
            ret, img = Capture.read()
            if ret:
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
                
                
                Qtformat = QImage(dst.data, dst.shape[1], dst.shape[0], QImage.Format_RGB888)
                self.ImageUpdate.emit(Qtformat)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

