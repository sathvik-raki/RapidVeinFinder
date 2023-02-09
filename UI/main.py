# Import libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy
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
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                Flippedimage = cv2.flip(Image, 1)
                Qtformat = QImage(Flippedimage.data, Flippedimage.shape[1], Flippedimage.shape[0], QImage.Format_RGB888)
                self.ImageUpdate.emit(Qtformat)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

