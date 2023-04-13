# Import libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from CapstonePY import Ui_MainWindow
import os
from sklearn.cluster import KMeans


# Define MainWindow class
class MainWindow():

    def __init__(self):
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
        self.ui.Background_darkness_slider.valueChanged.connect(self.set_Background_darkness)
        self.ui.AT_one_slider.valueChanged.connect(self.set_adaptiveThres_one)
        self.ui.AT_three_slider.valueChanged.connect(self.set_adaptiveThres_three)
        self.ui.Kmeans_slider.valueChanged.connect(self.set_Kmeans_tol)
        self.ui.GBlur_slider.valueChanged.connect(self.set_gaussianBlur)
        self.ui.Thres_one_slider.valueChanged.connect(self.set_thresh_one)
        self.ui.Thres_two_slider.valueChanged.connect(self.set_thresh_two)
        self.ui.camera_button.clicked.connect(self.change_cam_button_state)
        self.ui.save_button.clicked.connect(self.image_saving_function)
        self.ui.mode_one_button.clicked.connect(self.change_to_mode_one)
        self.ui.mode_two_button.clicked.connect(self.change_to_mode_two)
        self.ui.mode_three_button.clicked.connect(self.change_to_mode_three)

        # Set initial slider values
        self.ui.contrast_slider.setValue(10)
        self.ui.brightness_slider.setValue(5)
        self.ui.CCL_slider.setValue(15)
        self.ui.C_tile_slider.setValue(7)
        self.ui.Background_darkness_slider.setValue(50)
        self.ui.AT_one_slider.setValue(255)
        self.ui.AT_three_slider.setValue(255)
        self.ui.Kmeans_slider.setValue(50)
        self.ui.GBlur_slider.setValue(0)
        self.ui.Thres_one_slider.setValue(0)
        self.ui.Thres_two_slider.setValue(255)
        self.ui.AT_three_slider.setMaximum(1000)
        self.ui.C_tile_slider.setMinimum(1)
        self.ui.AT_one_slider.setMaximum(1000)
        self.ui.GBlur_slider.setMaximum(1000)
        self.ui.C_tile_slider.setMaximum(1000)
        self.ui.Background_darkness_slider.setMaximum(100)
        self.ui.Kmeans_slider.setMaximum(200)

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

    def change_to_mode_one(self):
        self.Pi_camera.mode_one_button_press = 1
        self.Pi_camera.mode_two_button_press = 0
        self.Pi_camera.mode_three_button_press = 0

    def change_to_mode_two(self):
        self.Pi_camera.mode_two_button_press = 1
        self.Pi_camera.mode_one_button_press = 0
        self.Pi_camera.mode_three_button_press = 0

    def change_to_mode_three(self):
        self.Pi_camera.mode_three_button_press = 1
        self.Pi_camera.mode_one_button_press = 0
        self.Pi_camera.mode_two_button_press = 0

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
            output_dir = r"./captures"
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
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.contrast = value/10
            self.ui.contrast_display.setText(str(self.Pi_camera.contrast))

    def set_brightness(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.brightness = value
            self.ui.brightness_display.setText(str(self.Pi_camera.brightness))

    def set_ClacheClipLimit(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.ClacheClipLimit = value/10
            self.ui.CCL_display.setText(str(self.Pi_camera.ClacheClipLimit))

    def set_ClacheTile_one(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.ClacheTile_one = value
            self.ui.C_Tile_display.setText(str(self.Pi_camera.ClacheTile_one))

    def set_Background_darkness(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.backgroundDarkness = value/100
            self.ui.Background_darkness_display.setText(str(self.Pi_camera.backgroundDarkness))

    def set_adaptiveThres_one(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.adaptiveThres_one = value
            self.ui.AT_one_display.setText(str(self.Pi_camera.adaptiveThres_one))

    def set_adaptiveThres_three(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.adaptiveThres_three = value/100
            self.ui.AT_three_display.setText(str(self.Pi_camera.adaptiveThres_three))

    def set_Kmeans_tol(self, value):
        if self.Pi_camera.mode_three_button_press == 1:
            self.Pi_camera.kmeansTolerance = value
            self.ui.Kmeans_display.setText(str(self.Pi_camera.kmeansTolerance))

    def set_gaussianBlur(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.gaussianBlur = value
            self.ui.G_blur_display.setText(str(self.Pi_camera.gaussianBlur))

    def set_thresh_one(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.thresh_one = value
            self.ui.Thres_one_display.setText(str(self.Pi_camera.thresh_one))

    def set_thresh_two(self, value):
        if self.Pi_camera.mode_two_button_press == 1:
            self.Pi_camera.thresh_two = value
            self.ui.Thres_two_display.setText(str(self.Pi_camera.thresh_two))

#Define Pi_camera class

class Pi_camera(QThread):

    # Define signals to be emitted to MainWindow class
    ImageUpdate_video = pyqtSignal(QImage)
    ImageUpdate_settings = pyqtSignal(QImage)
    ImageUpdate_camera = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self.contrast = 1
        self.brightness = 5.0
        self.cam_button_press = 0
        self.ClacheClipLimit = 1.2
        self.ClacheTile_one = 7
        self.ClacheTile_two = self.ClacheTile_one
        self.medianBlur = 5
        self.adaptiveThres_one = 255
        self.adaptiveThres_two = 255
        self.adaptiveThres_three = 7
        self.gaussianBlurTile_one = 5
        self.gaussianBlurTile_two = self.gaussianBlurTile_one
        self.gaussianBlur = 0
        self.thresh_one = 0
        self.thresh_two = 255
        self.mode_one_button_press = 1
        self.mode_two_button_press = 0
        self.mode_three_button_press = 0
        self.backgroundDarkness = 0.5
        self.kmeansTolerance = 50


    def video_processor(self, img):
        #img = cv2.imread("imageTest2.png", cv2.IMREAD_COLOR)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply a median blur to reduce noise
        img_blur = cv2.medianBlur(img, 5)

        # Apply thresholding to binarize the image
        _, img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # Perform morphological operations to remove noise and fill gaps
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
        img_morph = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)

        # Darken the pixels corresponding to the veins in the original image
        img_with_veins = np.copy(img)
        img_with_veins[img_morph==255] = (img_with_veins[img_morph==255] * self.backgroundDarkness).astype(np.uint8)
        img = img_with_veins
        


        img = cv2.resize(img, (240, 240)) 
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = np.array(img)
        # img = data.flatten()
        # img= img.reshape(240, 240)
        
        img = cv2.convertScaleAbs(img, alpha=self.contrast, beta=self.brightness)

        # Create a CLAHE object (Arguments are optional)
        clahe = cv2.createCLAHE(clipLimit=self.ClacheClipLimit, tileGridSize=(self.ClacheTile_one, self.ClacheTile_two))
        cl1 = clahe.apply(img)

        # Apply adaptive threshold
        cl2 = cv2.medianBlur(cl1, self.medianBlur)
        th1 = cv2.adaptiveThreshold(cl2, self.adaptiveThres_one, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, self.adaptiveThres_two, self.adaptiveThres_three)

        # Apply OTSU threshold
        blur = cv2.GaussianBlur(cl1, (self.gaussianBlurTile_one, self.gaussianBlurTile_two), self.gaussianBlur)
        _, th3 = cv2.threshold(blur, self.thresh_one, self.thresh_two, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        # Removing noise
        th2 = th1 & th3
        
        kernel = np.ones((1, 1), np.uint8)

        # Morphological transform
        opening = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel)

        # Finding outlines via contouring process
        contours,_ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        img1 = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        dst = cv2.drawContours(img1, contours, -1, (0, 255, 0), -1)

        return dst

    def template_matching(self, img):

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        no_of_templates = 20

        for i in range(1,no_of_templates+1):
            template = cv2.imread('images/template'+str(i)+'.png',0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(gray,template,cv2.TM_SQDIFF)
            _, _, min_loc, _ = cv2.minMaxLoc(res)
            top_left = min_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(img,top_left, bottom_right, 255, 1)
            cv2.putText(img, 'Detected Vein: '+str(i), (top_left[0],top_left[1]-10), 
                cv2.FONT_HERSHEY_PLAIN, 1.0, (255,255,255))
        
        return img

    def kmeans_algorithm(self, img, tolerance):
        
        img = self.video_processor(img)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply a Gaussian blur to reduce noise
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold the image to create a binary mask of the veins
        _, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)

        # Convert the binary mask to a color image
        mask = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

        # Reshape the image to a 2D array of pixels
        reshaped_img = img.reshape(-1, 3)

        # Use K-means clustering to segment the image into k clusters
        k = 3
        kmeans = KMeans(n_clusters=k, n_init=10)
        kmeans.fit(reshaped_img)

        # Get the mask for the pixels that belong to the veins
        mask = np.zeros((reshaped_img.shape[0],), dtype=np.bool_)
        for i in range(k):
            centroid = kmeans.cluster_centers_[i]
            distance = np.sqrt(np.sum((reshaped_img - centroid)**2, axis=1))
            mask |= distance < tolerance

        # Reshape the mask to match the original image shape
        mask = mask.reshape(img.shape[0], img.shape[1])

        # Apply the mask to the original image to highlight the veins in red
        masked_img = cv2.bitwise_and(img, img, mask=mask.astype(np.uint8))
        masked_img[mask] = [0, 0, 255]

        
        return masked_img

    def run(self):
        self.ThreadActive = True

        Capture = cv2.VideoCapture(0)

        processed_feed = None
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:

                if self.mode_one_button_press == 1:
                    processed_feed = self.template_matching(frame)
                elif self.mode_two_button_press == 1:
                    processed_feed = self.video_processor(frame)
                elif self.mode_three_button_press == 1:
                    processed_feed = self.kmeans_algorithm(frame, self.kmeansTolerance)

                if processed_feed is not None:

                    Qtformat = QImage(processed_feed.data, processed_feed.shape[1], processed_feed.shape[0], QImage.Format_RGB888)
                    Qtformat_scaled_video = Qtformat.scaled(279, 530, Qt.KeepAspectRatio)
                    Qtformat_scaled_settings = Qtformat.scaled(289, 250, Qt.KeepAspectRatio)
                    self.ImageUpdate_video.emit(Qtformat_scaled_video)
                    self.ImageUpdate_settings.emit(Qtformat_scaled_settings)

                if self.cam_button_press == 1:
                    if self.mode_one_button_press == 1:
                        processed_frame = self.template_matching(frame)
                    elif self.mode_two_button_press == 1:
                        processed_frame = self.video_processor(frame)
                    elif self.mode_three_button_press == 1:
                        processed_frame = self.kmeans_algorithm(frame, self.kmeansTolerance)

                    Qtformat = QImage(processed_frame.data, processed_frame.shape[1], processed_frame.shape[0], QImage.Format_RGB888)
                    Qtformat_scaled_picture = Qtformat.scaled(301, 594, Qt.KeepAspectRatio)
                    self.ImageUpdate_camera.emit(Qtformat_scaled_picture)
                    self.cam_button_press = 0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

