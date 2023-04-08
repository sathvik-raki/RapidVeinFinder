# Import libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from CapstonePY import Ui_MainWindow
import os

# Define MainWindow class
class MainWindow():

    def __init__(self,):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # Load animation
        self.animation = QPropertyAnimation(self.ui.side_menu, b'geometry')
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        # Initialize Pi_camera class and connect signals from Pi_camera class to slots in MainWindow class
        self.Pi_camera = Pi_camera()
        self.Pi_camera.start()
        self.Pi_camera.ImageUpdate_video.connect(self.video_label_slot)
        self.Pi_camera.ImageUpdate_settings.connect(self.setting_video_label_slot)
        self.Pi_camera.ImageUpdate_camera.connect(self.image_label_slot)

        # Setup landing page
        self.ui.stackedWidget.setCurrentWidget(self.ui.video_page)

        # Autoscale video feed/images
        self.ui.video_label.setScaledContents(True)
        self.ui.vid_setting_label.setScaledContents(True)
        self.ui.image_label.setScaledContents(True)

        # Add functionality to the buttons and sliders by connecting signals and slots in the MainWindow class
        self.ui.video_button.clicked.connect(self.show_video_page)
        self.ui.setting_button.clicked.connect(self.show_setting_page)
        self.ui.image_button.clicked.connect(self.show_image_page)
        self.ui.info_button.clicked.connect(self.show_info_page)
        self.ui.menu_button.clicked.connect(self.animate_side_menu)
        self.ui.contrast_slider.valueChanged.connect(self.set_contrast)
        self.ui.brightness_slider.valueChanged.connect(self.set_brightness)
        self.ui.CCL_slider.valueChanged.connect(self.set_ClacheClipLimit)
        self.ui.C_tile_slider.valueChanged.connect(self.set_ClacheTile_one)
        self.ui.M_blur_slider.valueChanged.connect(self.set_medianBlur)
        self.ui.AT_one_slider.valueChanged.connect(self.set_adaptiveThres_one)
        self.ui.AT_two_slider.valueChanged.connect(self.set_adaptiveThres_two)
        self.ui.AT_three_slider.valueChanged.connect(self.set_adaptiveThres_three)
        self.ui.GBT_slider.valueChanged.connect(self.set_gaussianBlurTile_one)
        self.ui.GBlur_slider.valueChanged.connect(self.set_gaussianBlur)
        self.ui.Thres_one_slider.valueChanged.connect(self.set_thresh_one)
        self.ui.Thres_two_slider.valueChanged.connect(self.set_thresh_two)
        self.ui.camera_button.clicked.connect(self.change_cam_button_state)
        self.ui.save_button.clicked.connect(self.image_saving_function)

        # Set initial values of parameters
        self.ui.contrast_slider.setValue(10)
        self.ui.brightness_slider.setValue(5)
        self.ui.CCL_slider.setValue(15)
        self.ui.C_tile_slider.setValue(7)
        self.ui.M_blur_slider.setValue(5) #Unstable
        self.ui.AT_one_slider.setValue(255)
        self.ui.AT_two_slider.setValue(25) #Unstable
        self.ui.AT_three_slider.setValue(255)
        self.ui.GBT_slider.setValue(5) #Unstable
        self.ui.GBlur_slider.setValue(0) 
        self.ui.Thres_one_slider.setValue(0)
        self.ui.Thres_two_slider.setValue(255)
        self.ui.AT_three_slider.setMaximum(1000)
        self.ui.C_tile_slider.setMinimum(1)
        self.ui.AT_one_slider.setMaximum(1000)
        self.ui.GBlur_slider.setMaximum(1000) 
        self.ui.C_tile_slider.setMaximum(1000)
    # Define what will be shown when buttons are clicked
    def show(self):
        self.main_win.show()

    def show_video_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.video_page)

    def show_setting_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page)

    def show_image_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.image_page)

    def show_info_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.info_page)

    # Function to change camera button state when button is pressed
    def change_cam_button_state(self):
        self.Pi_camera.cam_button_press = 1

    # Functions to convert signals from Pi_camera class to pixmap and attach to labels
    def video_label_slot(self, Image):
        self.ui.video_label.setPixmap(QPixmap.fromImage(Image))

    def setting_video_label_slot(self, Image):
        self.ui.vid_setting_label.setPixmap(QPixmap.fromImage(Image))

    def image_label_slot(self, Image):
        self.ui.image_label.setPixmap(QPixmap.fromImage(Image))

    # Image saving function
    def image_saving_function(self):

        pixmap = self.ui.image_label.pixmap()
        # Saves only saves image if pixmap is found
        if pixmap is not None:
            Image = pixmap.toImage()
            output_dir = r"C:\Users\jesse\Desktop\CapstoneImages"
            ImageName = "image"
            output_format = "jpg"
            count = 0

            # Loop saves images with different names
            while True:
                count += 1
                output_path = output_dir + "/" + ImageName + "_" + str(count) + "." + "jpg"
                if not os.path.exists(output_path):
                    break

            self.ui.image_label.setPixmap(QPixmap())
            Image.save(output_path, output_format)

    # Animation function
    def animate_side_menu(self):
        if self.ui.side_menu.isVisible():
            self.animation.setStartValue(self.ui.side_menu.geometry())
            self.animation.setEndValue(QRect(self.ui.side_menu.x(), self.ui.side_menu.y(), self.ui.side_menu.width(), 0))
            self.ui.side_menu.hide()
        else:
            # If menu bar is hidden, set animation to show it
            self.ui.side_menu.show()
            self.animation.setStartValue(QRect(self.ui.side_menu.x(), self.ui.side_menu.y(), self.ui.side_menu.width(), 0))
            self.animation.setEndValue(self.ui.side_menu.geometry())
        self.animation.start()

    # Set parameters functions
    def set_contrast(self, value):
        self.Pi_camera.contrast = value/10
        self.ui.contrast_display.setText(str(self.Pi_camera.contrast))

    def set_brightness(self, value):
        self.Pi_camera.brightness = value
        self.ui.brightness_display.setText(str(self.Pi_camera.brightness))

    def set_ClacheClipLimit(self, value):
        self.Pi_camera.ClacheClipLimit = value/10
        self.ui.CCL_display.setText(str(self.Pi_camera.ClacheClipLimit))

    def set_ClacheTile_one(self, value):
        self.Pi_camera.ClacheTile_one = value
        self.ui.C_Tile_display.setText(str(self.Pi_camera.ClacheTile_one))

    def set_medianBlur(self, value):
        self.Pi_camera.medianBlur = value
        self.ui.median_blur_display.setText(str(self.Pi_camera.medianBlur))

    def set_adaptiveThres_one(self, value):
        self.Pi_camera.adaptiveThres_one = value
        self.ui.AT_one_display.setText(str(self.Pi_camera.adaptiveThres_one))

    def set_adaptiveThres_two(self, value):
        self.Pi_camera.adaptiveThres_two = value
        self.ui.AT_two_display.setText(str(self.Pi_camera.adaptiveThres_two))

    def set_adaptiveThres_three(self, value):
        self.Pi_camera.adaptiveThres_three = value/100
        self.ui.AT_three_display.setText(str(self.Pi_camera.adaptiveThres_three))

    def set_gaussianBlurTile_one(self, value):
        self.Pi_camera.gaussianBlurTile_one = value
        self.ui.GBT_one_display.setText(str(self.Pi_camera.gaussianBlurTile_one))

    def set_gaussianBlur(self, value):
        self.Pi_camera.gaussianBlur = value
        self.ui.G_blur_display.setText(str(self.Pi_camera.gaussianBlur))

    def set_thresh_one(self, value):
        self.Pi_camera.thresh_one = value
        self.ui.Thres_one_display.setText(str(self.Pi_camera.thresh_one))

    def set_thresh_two(self, value):
        self.Pi_camera.thresh_two = value
        self.ui.Thres_two_display.setText(str(self.Pi_camera.thresh_two))
        
def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''

    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
    return arr
        
def image_processor(img):
    #cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
    #img = cv2.imread("imageTest2.png", cv2.IMREAD_COLOR)

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
    
    img = cv2.resize(img, (240, 240)) 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    data = np.array(img)
    img = data.flatten()
    img= img.reshape(240, 240)
    
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
    #cv2.imwrite("out.jpg", dst)
    
    #cv2.imshow("Live", dst)
    
    print("D")
    return dst

# Define Pi camera class

class Pi_camera(QThread):

    # Define signals to be emitted to MainWindow class
    ImageUpdate_video = pyqtSignal(QImage)
    ImageUpdate_settings = pyqtSignal(QImage)
    ImageUpdate_camera = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.contrast = 1.0
        self.brightness = 5.0
        self.cam_button_press = 0
        self.ClacheClipLimit = 1.5
        self.ClacheTile_one = 7
        self.ClacheTile_two = self.ClacheTile_one
        self.medianBlur = 5
        self.adaptiveThres_one = 255
        self.adaptiveThres_two = 25
        self.adaptiveThres_three = 2.55
        self.gaussianBlurTile_one = 5
        self.gaussianBlurTile_two = self.gaussianBlurTile_one
        self.gaussianBlur = 0
        self.thresh_one = 0
        self.thresh_two = 255

    def run(self):
        self.ThreadActive = True

        
        Capture = cv2.VideoCapture(0)
        #Capture = cv2.VideoCapture('filename2.avi')
        
        frame_width = int(Capture.get(3))
        frame_height = int(Capture.get(4))   
        size = (frame_width, frame_height)
        result = cv2.VideoWriter('fil2.avi',  cv2.VideoWriter_fourcc(*'MJPG'),10, size)
        
        
        while self.ThreadActive:
            ret, img = Capture.read()
            if ret:
                # kernel = np.ones((1, 1), np.uint8)
                #Simg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # img = cv2.convertScaleAbs(img, alpha=self.contrast, beta=self.brightness)

                # # Create a CLAHE object (Arguments are optional)
                # clahe = cv2.createCLAHE(clipLimit=self.ClacheClipLimit, tileGridSize=(self.ClacheTile_one, self.ClacheTile_two))
                # cl1 = clahe.apply(img)

                # # Apply adaptive threshold
                # cl2 = cv2.medianBlur(cl1, self.medianBlur)
                # th1 = cv2.adaptiveThreshold(cl2, self.adaptiveThres_one, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, self.adaptiveThres_two, self.adaptiveThres_three)

                # # Apply OTSU threshold
                # blur = cv2.GaussianBlur(cl1, (self.gaussianBlurTile_one, self.gaussianBlurTile_two), self.gaussianBlur)
                # ret3, th3 = cv2.threshold(blur, self.thresh_one, self.thresh_two, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

                # # Removing noise
                # th2 = th1 & th3

                # # Morphological transform
                # opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

                # # Finding outlines via contouring process
                # contours, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                # img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                # dst = cv2.drawContours(img1, contours, -1, (0, 255, 0), -1)
                # openingImg = cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR)
                
                # result.write(dst)

                # Scale video feed before emitting
                #Qtformat = QImage(openingImg.data, openingImg.shape[1], openingImg.shape[0], QImage.Format_RGB888)
                Qtformat = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
                Qtformat_scaled_video = Qtformat.scaled(301, 594, Qt.KeepAspectRatio)
                Qtformat_scaled_settings = Qtformat.scaled(289, 300, Qt.KeepAspectRatio)

                # Capture a frame, scale and emit for image page(camera)
                if self.cam_button_press == 1:
                    Qtformat_scaled_camera = Qtformat.scaled(301, 594, Qt.KeepAspectRatio)

                    #print(type(Qtformat_scaled_camera))
                    cv2_img = convertQImageToMat(Qtformat_scaled_camera)
                    returned = image_processor(cv2_img)
                    height, width, channel = returned.shape
                    bytesPerLine = 3 * width
                    qImg = QImage(returned.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                    self.ImageUpdate_camera.emit(qImg)
                    
                    
                self.cam_button_press = 0

                # Emit video feed for video and setting pages
                self.ImageUpdate_video.emit(Qtformat_scaled_video)
                self.ImageUpdate_settings.emit(Qtformat_scaled_settings)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

