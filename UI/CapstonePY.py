# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CapstoneUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(480, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/more-horizontal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("*{\n"
"   background-color:transparent;\n"
"}\n"
"\n"
"#centralwidget{\n"
"   background-color:transparent;\n"
"}\n"
"\n"
"QPushButton{\n"
"   padding: 10px;\n"
"   background-color:white;\n"
"}\n"
"\n"
"QToolButton{\n"
"   padding:10px;\n"
"   background-color:white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:rgb(215,214,213);\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"background-color:rgb(215,214,213);\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_frame = QtWidgets.QFrame(self.header)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.button_frame.setFont(font)
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_button = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy)
        self.menu_button.setMinimumSize(QtCore.QSize(0, 33))
        self.menu_button.setMaximumSize(QtCore.QSize(16777215, 33))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.menu_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_button.setIcon(icon1)
        self.menu_button.setObjectName("menu_button")
        self.horizontalLayout_3.addWidget(self.menu_button)
        self.horizontalLayout_2.addWidget(self.button_frame, 0, QtCore.Qt.AlignLeft)
        self.logo_frame = QtWidgets.QFrame(self.header)
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.logo_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.product_name = QtWidgets.QLabel(self.logo_frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.product_name.setFont(font)
        self.product_name.setAlignment(QtCore.Qt.AlignCenter)
        self.product_name.setObjectName("product_name")
        self.horizontalLayout_4.addWidget(self.product_name)
        self.horizontalLayout_2.addWidget(self.logo_frame)
        self.verticalLayout.addWidget(self.header)
        self.body = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QFrame(self.body)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_container = QtWidgets.QFrame(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_container.sizePolicy().hasHeightForWidth())
        self.menu_container.setSizePolicy(sizePolicy)
        self.menu_container.setMinimumSize(QtCore.QSize(100, 0))
        self.menu_container.setMaximumSize(QtCore.QSize(100, 16777215))
        self.menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_container.setObjectName("menu_container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_container)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.video_button = QtWidgets.QToolButton(self.menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_button.sizePolicy().hasHeightForWidth())
        self.video_button.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/video.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.video_button.setIcon(icon2)
        self.video_button.setObjectName("video_button")
        self.verticalLayout_3.addWidget(self.video_button)
        self.setting_button = QtWidgets.QToolButton(self.menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_button.sizePolicy().hasHeightForWidth())
        self.setting_button.setSizePolicy(sizePolicy)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_button.setIcon(icon3)
        self.setting_button.setObjectName("setting_button")
        self.verticalLayout_3.addWidget(self.setting_button)
        self.image_button = QtWidgets.QToolButton(self.menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_button.sizePolicy().hasHeightForWidth())
        self.image_button.setSizePolicy(sizePolicy)
        self.image_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/image.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.image_button.setIcon(icon4)
        self.image_button.setObjectName("image_button")
        self.verticalLayout_3.addWidget(self.image_button)
        self.info_button = QtWidgets.QToolButton(self.menu_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info_button.setIcon(icon5)
        self.info_button.setObjectName("info_button")
        self.verticalLayout_3.addWidget(self.info_button)
        self.verticalLayout_2.addWidget(self.menu_container)
        self.horizontalLayout.addWidget(self.side_menu)
        self.video_frame = QtWidgets.QFrame(self.body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_frame.sizePolicy().hasHeightForWidth())
        self.video_frame.setSizePolicy(sizePolicy)
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.video_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.video_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.video_page = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_page.sizePolicy().hasHeightForWidth())
        self.video_page.setSizePolicy(sizePolicy)
        self.video_page.setStyleSheet("background-color: transparent;")
        self.video_page.setObjectName("video_page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.video_page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.feed_frame = QtWidgets.QFrame(self.video_page)
        self.feed_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.feed_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.feed_frame.setObjectName("feed_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.feed_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.video_label = QtWidgets.QLabel(self.feed_frame)
        self.video_label.setStyleSheet("background-color: white;")
        self.video_label.setText("")
        self.video_label.setObjectName("video_label")
        self.verticalLayout_4.addWidget(self.video_label)
        self.camera_button = QtWidgets.QPushButton(self.feed_frame)
        self.camera_button.setStyleSheet("\n"
"QPushButton#camera_button{\n"
"   padding: 10px;\n"
"   background-color:white;\n"
"}\n"
"\n"
"QPushButton:hover#camera_button {\n"
"background-color:rgb(215,214,213);\n"
"}")
        self.camera_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.camera_button.setIcon(icon6)
        self.camera_button.setObjectName("camera_button")
        self.verticalLayout_4.addWidget(self.camera_button)
        self.horizontalLayout_6.addWidget(self.feed_frame)
        self.stackedWidget.addWidget(self.video_page)
        self.setting_page = QtWidgets.QWidget()
        self.setting_page.setStyleSheet("background-color: transparent;")
        self.setting_page.setObjectName("setting_page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.setting_page)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame = QtWidgets.QFrame(self.setting_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.GBT_one_display = QtWidgets.QLabel(self.frame)
        self.GBT_one_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GBT_one_display.setText("")
        self.GBT_one_display.setObjectName("GBT_one_display")
        self.gridLayout.addWidget(self.GBT_one_display, 11, 3, 1, 1)
        self.GBlur_para = QtWidgets.QLabel(self.frame)
        self.GBlur_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GBlur_para.setObjectName("GBlur_para")
        self.gridLayout.addWidget(self.GBlur_para, 12, 0, 1, 1)
        self.CCL_slider = QtWidgets.QSlider(self.frame)
        self.CCL_slider.setMinimum(-100)
        self.CCL_slider.setMaximum(100)
        self.CCL_slider.setPageStep(1)
        self.CCL_slider.setProperty("value", 1)
        self.CCL_slider.setOrientation(QtCore.Qt.Horizontal)
        self.CCL_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.CCL_slider.setTickInterval(5)
        self.CCL_slider.setObjectName("CCL_slider")
        self.gridLayout.addWidget(self.CCL_slider, 3, 1, 1, 2)
        self.G_blur_display = QtWidgets.QLabel(self.frame)
        self.G_blur_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G_blur_display.setText("")
        self.G_blur_display.setObjectName("G_blur_display")
        self.gridLayout.addWidget(self.G_blur_display, 12, 3, 1, 1)
        self.AT_three_display = QtWidgets.QLabel(self.frame)
        self.AT_three_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AT_three_display.setText("")
        self.AT_three_display.setObjectName("AT_three_display")
        self.gridLayout.addWidget(self.AT_three_display, 8, 3, 1, 1)
        self.video_settings_frame = QtWidgets.QFrame(self.frame)
        self.video_settings_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_settings_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_settings_frame.setObjectName("video_settings_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.video_settings_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.vid_setting_label = QtWidgets.QLabel(self.video_settings_frame)
        self.vid_setting_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vid_setting_label.setText("")
        self.vid_setting_label.setObjectName("vid_setting_label")
        self.horizontalLayout_10.addWidget(self.vid_setting_label)
        self.gridLayout.addWidget(self.video_settings_frame, 0, 0, 1, 4)
        self.AT_three_para = QtWidgets.QLabel(self.frame)
        self.AT_three_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AT_three_para.setObjectName("AT_three_para")
        self.gridLayout.addWidget(self.AT_three_para, 8, 0, 1, 1)
        self.contrast_para = QtWidgets.QLabel(self.frame)
        self.contrast_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contrast_para.setObjectName("contrast_para")
        self.gridLayout.addWidget(self.contrast_para, 1, 0, 1, 1)
        self.contrast_display = QtWidgets.QLabel(self.frame)
        self.contrast_display.setStyleSheet("background-color: white;")
        self.contrast_display.setText("")
        self.contrast_display.setObjectName("contrast_display")
        self.gridLayout.addWidget(self.contrast_display, 1, 3, 1, 1)
        self.brightness_display = QtWidgets.QLabel(self.frame)
        self.brightness_display.setStyleSheet("background-color: white;")
        self.brightness_display.setText("")
        self.brightness_display.setObjectName("brightness_display")
        self.gridLayout.addWidget(self.brightness_display, 2, 3, 1, 1)
        self.CCLone_para = QtWidgets.QLabel(self.frame)
        self.CCLone_para.setStyleSheet("background-color: white;")
        self.CCLone_para.setObjectName("CCLone_para")
        self.gridLayout.addWidget(self.CCLone_para, 3, 0, 1, 1)
        self.CCL_display = QtWidgets.QLabel(self.frame)
        self.CCL_display.setStyleSheet("background-color: white;")
        self.CCL_display.setText("")
        self.CCL_display.setObjectName("CCL_display")
        self.gridLayout.addWidget(self.CCL_display, 3, 3, 1, 1)
        self.CTile_para = QtWidgets.QLabel(self.frame)
        self.CTile_para.setStyleSheet("background-color: white;")
        self.CTile_para.setObjectName("CTile_para")
        self.gridLayout.addWidget(self.CTile_para, 4, 0, 1, 1)
        self.contrast_slider = QtWidgets.QSlider(self.frame)
        self.contrast_slider.setMinimum(1)
        self.contrast_slider.setMaximum(30)
        self.contrast_slider.setSingleStep(1)
        self.contrast_slider.setPageStep(1)
        self.contrast_slider.setTracking(True)
        self.contrast_slider.setOrientation(QtCore.Qt.Horizontal)
        self.contrast_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.contrast_slider.setTickInterval(1)
        self.contrast_slider.setObjectName("contrast_slider")
        self.gridLayout.addWidget(self.contrast_slider, 1, 1, 1, 2)
        self.brightness_para = QtWidgets.QLabel(self.frame)
        self.brightness_para.setStyleSheet("background-color: white;")
        self.brightness_para.setObjectName("brightness_para")
        self.gridLayout.addWidget(self.brightness_para, 2, 0, 1, 1)
        self.AT_para = QtWidgets.QLabel(self.frame)
        self.AT_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AT_para.setObjectName("AT_para")
        self.gridLayout.addWidget(self.AT_para, 6, 0, 1, 1)
        self.C_Tile_display = QtWidgets.QLabel(self.frame)
        self.C_Tile_display.setStyleSheet("background-color: white;")
        self.C_Tile_display.setText("")
        self.C_Tile_display.setObjectName("C_Tile_display")
        self.gridLayout.addWidget(self.C_Tile_display, 4, 3, 1, 1)
        self.MBlur_para = QtWidgets.QLabel(self.frame)
        self.MBlur_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MBlur_para.setObjectName("MBlur_para")
        self.gridLayout.addWidget(self.MBlur_para, 5, 0, 1, 1)
        self.median_blur_display = QtWidgets.QLabel(self.frame)
        self.median_blur_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.median_blur_display.setText("")
        self.median_blur_display.setObjectName("median_blur_display")
        self.gridLayout.addWidget(self.median_blur_display, 5, 3, 1, 1)
        self.AT_one_display = QtWidgets.QLabel(self.frame)
        self.AT_one_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AT_one_display.setText("")
        self.AT_one_display.setObjectName("AT_one_display")
        self.gridLayout.addWidget(self.AT_one_display, 6, 3, 1, 1)
        self.AT_two_para = QtWidgets.QLabel(self.frame)
        self.AT_two_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AT_two_para.setObjectName("AT_two_para")
        self.gridLayout.addWidget(self.AT_two_para, 7, 0, 1, 1)
        self.AT_two_display = QtWidgets.QLabel(self.frame)
        self.AT_two_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.AT_two_display.setText("")
        self.AT_two_display.setObjectName("AT_two_display")
        self.gridLayout.addWidget(self.AT_two_display, 7, 3, 1, 1)
        self.GBT_para = QtWidgets.QLabel(self.frame)
        self.GBT_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.GBT_para.setObjectName("GBT_para")
        self.gridLayout.addWidget(self.GBT_para, 11, 0, 1, 1)
        self.Thres_one_display = QtWidgets.QLabel(self.frame)
        self.Thres_one_display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Thres_one_display.setText("")
        self.Thres_one_display.setObjectName("Thres_one_display")
        self.gridLayout.addWidget(self.Thres_one_display, 15, 3, 1, 1)
        self.Thres_two_display = QtWidgets.QLabel(self.frame)
        self.Thres_two_display.setStyleSheet("background-color: white;")
        self.Thres_two_display.setText("")
        self.Thres_two_display.setObjectName("Thres_two_display")
        self.gridLayout.addWidget(self.Thres_two_display, 16, 3, 1, 1)
        self.brightness_slider = QtWidgets.QSlider(self.frame)
        self.brightness_slider.setMinimum(-255)
        self.brightness_slider.setMaximum(255)
        self.brightness_slider.setPageStep(1)
        self.brightness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.brightness_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.brightness_slider.setTickInterval(10)
        self.brightness_slider.setObjectName("brightness_slider")
        self.gridLayout.addWidget(self.brightness_slider, 2, 1, 1, 2)
        self.C_tile_slider = QtWidgets.QSlider(self.frame)
        self.C_tile_slider.setMinimum(-100)
        self.C_tile_slider.setMaximum(100)
        self.C_tile_slider.setPageStep(1)
        self.C_tile_slider.setProperty("value", 1)
        self.C_tile_slider.setOrientation(QtCore.Qt.Horizontal)
        self.C_tile_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.C_tile_slider.setTickInterval(5)
        self.C_tile_slider.setObjectName("C_tile_slider")
        self.gridLayout.addWidget(self.C_tile_slider, 4, 1, 1, 2)
        self.M_blur_slider = QtWidgets.QSlider(self.frame)
        self.M_blur_slider.setMinimum(-100)
        self.M_blur_slider.setMaximum(100)
        self.M_blur_slider.setPageStep(1)
        self.M_blur_slider.setProperty("value", 1)
        self.M_blur_slider.setOrientation(QtCore.Qt.Horizontal)
        self.M_blur_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.M_blur_slider.setTickInterval(5)
        self.M_blur_slider.setObjectName("M_blur_slider")
        self.gridLayout.addWidget(self.M_blur_slider, 5, 1, 1, 2)
        self.AT_one_slider = QtWidgets.QSlider(self.frame)
        self.AT_one_slider.setMinimum(-255)
        self.AT_one_slider.setMaximum(255)
        self.AT_one_slider.setPageStep(1)
        self.AT_one_slider.setProperty("value", 1)
        self.AT_one_slider.setOrientation(QtCore.Qt.Horizontal)
        self.AT_one_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.AT_one_slider.setTickInterval(10)
        self.AT_one_slider.setObjectName("AT_one_slider")
        self.gridLayout.addWidget(self.AT_one_slider, 6, 1, 1, 2)
        self.AT_two_slider = QtWidgets.QSlider(self.frame)
        self.AT_two_slider.setMinimum(-100)
        self.AT_two_slider.setMaximum(100)
        self.AT_two_slider.setPageStep(1)
        self.AT_two_slider.setProperty("value", 1)
        self.AT_two_slider.setOrientation(QtCore.Qt.Horizontal)
        self.AT_two_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.AT_two_slider.setTickInterval(5)
        self.AT_two_slider.setObjectName("AT_two_slider")
        self.gridLayout.addWidget(self.AT_two_slider, 7, 1, 1, 2)
        self.AT_three_slider = QtWidgets.QSlider(self.frame)
        self.AT_three_slider.setMinimum(-255)
        self.AT_three_slider.setMaximum(255)
        self.AT_three_slider.setPageStep(1)
        self.AT_three_slider.setProperty("value", 1)
        self.AT_three_slider.setOrientation(QtCore.Qt.Horizontal)
        self.AT_three_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.AT_three_slider.setTickInterval(10)
        self.AT_three_slider.setObjectName("AT_three_slider")
        self.gridLayout.addWidget(self.AT_three_slider, 8, 1, 1, 2)
        self.GBT_slider = QtWidgets.QSlider(self.frame)
        self.GBT_slider.setMinimum(-100)
        self.GBT_slider.setMaximum(100)
        self.GBT_slider.setPageStep(1)
        self.GBT_slider.setProperty("value", 1)
        self.GBT_slider.setOrientation(QtCore.Qt.Horizontal)
        self.GBT_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.GBT_slider.setTickInterval(5)
        self.GBT_slider.setObjectName("GBT_slider")
        self.gridLayout.addWidget(self.GBT_slider, 11, 1, 1, 2)
        self.GBlur_slider = QtWidgets.QSlider(self.frame)
        self.GBlur_slider.setMinimum(-100)
        self.GBlur_slider.setMaximum(100)
        self.GBlur_slider.setPageStep(1)
        self.GBlur_slider.setProperty("value", 1)
        self.GBlur_slider.setOrientation(QtCore.Qt.Horizontal)
        self.GBlur_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.GBlur_slider.setTickInterval(5)
        self.GBlur_slider.setObjectName("GBlur_slider")
        self.gridLayout.addWidget(self.GBlur_slider, 12, 1, 1, 2)
        self.Thres_one_para = QtWidgets.QLabel(self.frame)
        self.Thres_one_para.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Thres_one_para.setObjectName("Thres_one_para")
        self.gridLayout.addWidget(self.Thres_one_para, 15, 0, 1, 1)
        self.Thres_two_para = QtWidgets.QLabel(self.frame)
        self.Thres_two_para.setStyleSheet("background-color: white;")
        self.Thres_two_para.setObjectName("Thres_two_para")
        self.gridLayout.addWidget(self.Thres_two_para, 16, 0, 1, 1)
        self.Thres_one_slider = QtWidgets.QSlider(self.frame)
        self.Thres_one_slider.setMinimum(-100)
        self.Thres_one_slider.setMaximum(100)
        self.Thres_one_slider.setPageStep(1)
        self.Thres_one_slider.setProperty("value", 1)
        self.Thres_one_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Thres_one_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Thres_one_slider.setTickInterval(5)
        self.Thres_one_slider.setObjectName("Thres_one_slider")
        self.gridLayout.addWidget(self.Thres_one_slider, 15, 1, 1, 2)
        self.Thres_two_slider = QtWidgets.QSlider(self.frame)
        self.Thres_two_slider.setMinimum(-255)
        self.Thres_two_slider.setMaximum(255)
        self.Thres_two_slider.setPageStep(1)
        self.Thres_two_slider.setProperty("value", 1)
        self.Thres_two_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Thres_two_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Thres_two_slider.setTickInterval(10)
        self.Thres_two_slider.setObjectName("Thres_two_slider")
        self.gridLayout.addWidget(self.Thres_two_slider, 16, 1, 1, 2)
        self.horizontalLayout_9.addWidget(self.frame)
        self.stackedWidget.addWidget(self.setting_page)
        self.image_page = QtWidgets.QWidget()
        self.image_page.setStyleSheet("background-color: transparent;")
        self.image_page.setObjectName("image_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.image_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.image_frame = QtWidgets.QFrame(self.image_page)
        self.image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.image_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.image_label = QtWidgets.QLabel(self.image_frame)
        self.image_label.setStyleSheet("background-color: white;")
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.verticalLayout_5.addWidget(self.image_label)
        self.save_button = QtWidgets.QPushButton(self.image_frame)
        self.save_button.setStyleSheet("QPushButton#save_button{\n"
"   padding: 10px;\n"
"   background-color:white;\n"
"}\n"
"\n"
"QPushButton:hover#save_button {\n"
"background-color:rgb(215,214,213);\n"
"}")
        self.save_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon7)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_5.addWidget(self.save_button)
        self.horizontalLayout_7.addWidget(self.image_frame)
        self.stackedWidget.addWidget(self.image_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setStyleSheet("background-color: transparent;")
        self.info_page.setObjectName("info_page")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.info_page)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.info_label = QtWidgets.QLabel(self.info_page)
        self.info_label.setText("")
        self.info_label.setObjectName("info_label")
        self.horizontalLayout_8.addWidget(self.info_label)
        self.stackedWidget.addWidget(self.info_page)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.video_frame)
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PROTOTYPE"))
        self.menu_button.setText(_translate("MainWindow", "MENU"))
        self.product_name.setText(_translate("MainWindow", "MR-VEIN"))
        self.video_button.setText(_translate("MainWindow", "VIDEO"))
        self.setting_button.setText(_translate("MainWindow", "CONTRAST"))
        self.info_button.setText(_translate("MainWindow", "INFO"))
        self.GBlur_para.setText(_translate("MainWindow", "G.Blur:"))
        self.AT_three_para.setText(_translate("MainWindow", "A.T Three:"))
        self.contrast_para.setText(_translate("MainWindow", "Contrast:"))
        self.CCLone_para.setText(_translate("MainWindow", "CCL One:"))
        self.CTile_para.setText(_translate("MainWindow", "C.Tile One:"))
        self.brightness_para.setText(_translate("MainWindow", "Brightness:"))
        self.AT_para.setText(_translate("MainWindow", "A.T One:"))
        self.MBlur_para.setText(_translate("MainWindow", "M.Blur:"))
        self.AT_two_para.setText(_translate("MainWindow", "A.T Two:"))
        self.GBT_para.setText(_translate("MainWindow", "G.B.T One:"))
        self.Thres_one_para.setText(_translate("MainWindow", "T.H One:"))
        self.Thres_two_para.setText(_translate("MainWindow", "T.H Two:"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
