# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 672)

        # font settings
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        # central widget 
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")


        # --------------------header widget start--------------------

        # header widget
        self.header = QtWidgets.QWidget(self.centralwidget)
        self.header.setObjectName("header")

        # menu button
        self.menu_btn = QtWidgets.QPushButton(self.header)
        self.menu_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/activity-feed-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_btn.setIcon(icon)
        self.menu_btn.setIconSize(QtCore.QSize(20, 20))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)
        self.menu_btn.setAutoExclusive(True)
        self.menu_btn.setObjectName("menu_btn")

        # vertical spacer between menu button and face recognition label
        spacerItem = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # face recognition label
        self.fr_label = QtWidgets.QLabel(self.header)
        self.fr_label.setScaledContents(True)
        self.fr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fr_label.setObjectName("fr_label")

        # vertical spacer between face recognition label and end of screen
        spacerItem1 = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        # header widget in horizontal layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.menu_btn)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.fr_label)
        self.horizontalLayout_2.addItem(spacerItem1)


        # --------------------header widget end--------------------



        # --------------------sidebar widget start--------------------

        # sidebar widget
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setObjectName("sidebar")

        # home button
        self.home_btn = QtWidgets.QPushButton(self.sidebar)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QtCore.QSize(20, 20))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)
        self.home_btn.setObjectName("home_btn")

        # add data button
        self.add_data_btn = QtWidgets.QPushButton(self.sidebar)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/add-database-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_data_btn.setIcon(icon2)
        self.add_data_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_data_btn.setCheckable(True)
        self.add_data_btn.setAutoExclusive(True)
        self.add_data_btn.setObjectName("add_data_btn")

        # recognize face button
        self.recg_face_btn = QtWidgets.QPushButton(self.sidebar)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/Face_Recognize13.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recg_face_btn.setIcon(icon3)
        self.recg_face_btn.setIconSize(QtCore.QSize(20, 20))
        self.recg_face_btn.setCheckable(True)
        self.recg_face_btn.setAutoExclusive(True)
        self.recg_face_btn.setObjectName("recg_face_btn")

        # settings panel button
        self.sett_panel_btn = QtWidgets.QPushButton(self.sidebar)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/settings-17-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sett_panel_btn.setIcon(icon4)
        self.sett_panel_btn.setIconSize(QtCore.QSize(20, 20))
        self.sett_panel_btn.setCheckable(True)
        self.sett_panel_btn.setAutoExclusive(True)
        self.sett_panel_btn.setObjectName("sett_panel_btn")

        # add camera button
        self.add_camera_btn = QtWidgets.QPushButton(self.sidebar)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/add-photo-camera1.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_camera_btn.setIcon(icon5)
        self.add_camera_btn.setIconSize(QtCore.QSize(20, 20))
        self.add_camera_btn.setCheckable(True)
        self.add_camera_btn.setAutoExclusive(True)
        self.add_camera_btn.setObjectName("add_camera_btn")

        # test video button
        self.test_video_btn = QtWidgets.QPushButton(self.sidebar)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/add-file-path2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.test_video_btn.setIcon(icon6)
        self.test_video_btn.setIconSize(QtCore.QSize(20, 20))
        self.test_video_btn.setCheckable(True)
        self.test_video_btn.setAutoExclusive(True)
        self.test_video_btn.setObjectName("test_video_btn")
        
        # above buttons in vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.home_btn)
        self.verticalLayout.addWidget(self.add_data_btn)
        self.verticalLayout.addWidget(self.recg_face_btn)
        self.verticalLayout.addWidget(self.sett_panel_btn)
        self.verticalLayout.addWidget(self.add_camera_btn)
        self.verticalLayout.addWidget(self.test_video_btn)

        # vertical spacer between vertical layout of buttons and close button
        spacerItem2 = QtWidgets.QSpacerItem(20, 399, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # close button
        self.close_btn = QtWidgets.QPushButton(self.sidebar)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon7)
        self.close_btn.setIconSize(QtCore.QSize(20, 20))
        self.close_btn.setCheckable(True)
        self.close_btn.setAutoExclusive(True)
        self.close_btn.setObjectName("close_btn")
        
        # set of buttons, vertical spacer and close button in vertical layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.close_btn)


        # --------------------sidebar widget end--------------------



        # --------------------content page widget start--------------------        

        # content page
        self.content_page = QtWidgets.QWidget(self.centralwidget)
        self.content_page.setObjectName("content_page")

        # stacked widget
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_page)
        self.stackedWidget.setObjectName("stackedWidget")


        # --------------------home page start--------------------

        # home page
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        # home page in label
        self.home_page_label = QtWidgets.QLabel(self.home_page)
        self.home_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_page_label.setObjectName("home_page_label")
        self.gridLayout_2.addWidget(self.home_page_label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.home_page)


        # --------------------home page page end--------------------



        # --------------------add data page start--------------------

        # add data page
        self.add_data_page = QtWidgets.QWidget()
        self.add_data_page.setObjectName("add_data_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.add_data_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # add data label
        self.label_3 = QtWidgets.QLabel(self.add_data_page)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_data_page)


        # --------------------add data page end--------------------


        # --------------------recognize face page start--------------------

        # recognize face page
        self.recg_face_page = QtWidgets.QWidget()
        self.recg_face_page.setObjectName("recg_face_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.recg_face_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        # recognize face label
        self.label_4 = QtWidgets.QLabel(self.recg_face_page)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.recg_face_page)


        # --------------------recognize face page end--------------------



        # --------------------settings panel page start--------------------

        # settings panel page
        self.sett_panel_page = QtWidgets.QWidget()
        self.sett_panel_page.setObjectName("sett_panel_page")


        # settings panel label
        self.sett_panel_label = QtWidgets.QLabel(self.sett_panel_page)
        self.sett_panel_label.setScaledContents(True)
        self.sett_panel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sett_panel_label.setObjectName("sett_panel_label")

        # 4 spacers
        # SP = settings panel, T = top, L = left, R = right, B = bottom, S = spacer
        SPTS = QtWidgets.QSpacerItem(20, 133, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        SPLS = QtWidgets.QSpacerItem(71, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        SPRS = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        SPBS = QtWidgets.QSpacerItem(20, 133, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # detection model label
        self.detection_model_label = QtWidgets.QLabel(self.sett_panel_page)
        self.detection_model_label.setMinimumSize(QtCore.QSize(220, 25))
        self.detection_model_label.setScaledContents(True)
        self.detection_model_label.setAlignment(QtCore.Qt.AlignCenter)
        self.detection_model_label.setObjectName("detection_model_label")
        # detection model combobox
        self.detection_model_CB = QtWidgets.QComboBox(self.sett_panel_page)
        self.detection_model_CB.setMinimumSize(QtCore.QSize(200, 20))
        self.detection_model_CB.setObjectName("detection_model_CB")
        self.detection_model_index = {0:"MTCNN",1:"mediapipe"}
        self.detection_model_CB.addItems(['MTCNN', 'mediapipe'])
        self.detection_model_CB.setCurrentIndex(1)
        # horizontal spacer between detection model label and detection model combobox
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # detection model cell in horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.detection_model_label)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout.addWidget(self.detection_model_CB)

        # vertical spacer between detection model cell and recognition model cell
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # recognition model label
        self.recognition_model_label = QtWidgets.QLabel(self.sett_panel_page)
        self.recognition_model_label.setMinimumSize(QtCore.QSize(220, 25))
        self.recognition_model_label.setScaledContents(True)
        self.recognition_model_label.setAlignment(QtCore.Qt.AlignCenter)
        self.recognition_model_label.setObjectName("recognition_model_label")
        # recognition model combobox
        self.recognition_model_CB = QtWidgets.QComboBox(self.sett_panel_page)
        self.recognition_model_CB.setMinimumSize(QtCore.QSize(200, 20))
        self.recognition_model_CB.setObjectName("recognition_model_CB")
        self.recognition_model_CB.addItems(['FaceNet512', 'ArcFace'])
        # horizontal spacer between recognition model label and recognition model combobox
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # recognition model cell in horizontal layout
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.addWidget(self.recognition_model_label)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_3.addWidget(self.recognition_model_CB)

        # vertical spacer between recognition model cell and processors cell
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        # processor label
        self.processors_label = QtWidgets.QLabel(self.sett_panel_page)
        self.processors_label.setMinimumSize(QtCore.QSize(220, 25))
        self.processors_label.setScaledContents(True)
        self.processors_label.setAlignment(QtCore.Qt.AlignCenter)
        self.processors_label.setObjectName("processors_label")
        # processor combobox 
        self.processors_CB = QtWidgets.QComboBox(self.sett_panel_page)
        self.processors_CB.setMinimumSize(QtCore.QSize(200, 20))
        self.processors_CB.setObjectName("processors_CB")
        # add number of processors
        cpu_count = os.cpu_count()
        processors = []
        for i in range(2, cpu_count+1):
            processors.append(str(i))
        self.processors_CB.addItems(processors)
        # horizontal spacer between processor label and processor combobox
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # processors cell in horizontal layout
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.addWidget(self.processors_label)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_4.addWidget(self.processors_CB)

        # vertical spacer between processors cell and save settings button
        processorsCellSaveBtnCellSpacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        # save settings button
        self.save_sett_btn = QtWidgets.QPushButton(self.sett_panel_page)
        self.save_sett_btn.setObjectName("save_sett_btn")

        # detection model cell, recognition model cell, processors cell, 
        # save settings button and vertical spacers in vertical layout
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addItem(processorsCellSaveBtnCellSpacer)
        self.verticalLayout_3.addWidget(self.save_sett_btn)

        # all elements of settings panel in grid layout
        self.settPanelGL = QtWidgets.QGridLayout(self.sett_panel_page)
        self.settPanelGL.setObjectName("settPanelGL")
        self.settPanelGL.addWidget(self.sett_panel_label, 0, 1, 1, 2)
        self.settPanelGL.addItem(SPTS, 1, 1, 1, 1)
        self.settPanelGL.addItem(SPLS, 2, 0, 1, 1)
        self.settPanelGL.addLayout(self.verticalLayout_3, 2, 1, 1, 2)
        self.settPanelGL.addItem(SPRS, 2, 3, 1, 1)
        self.settPanelGL.addItem(SPBS, 3, 2, 1, 1)
        
        self.stackedWidget.addWidget(self.sett_panel_page)


        # --------------------settings panel page end--------------------



        # --------------------add camera page start--------------------

        # add camera page
        self.add_camera_page = QtWidgets.QWidget()
        self.add_camera_page.setObjectName("add_camera_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.add_camera_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        # add camera label
        self.label_6 = QtWidgets.QLabel(self.add_camera_page)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_camera_page)

        # --------------------add camera page end--------------------



        # --------------------add filepath page start--------------------

        # add filepath page
        self.add_fp_page = QtWidgets.QWidget()
        self.add_fp_page.setObjectName("add_fp_page")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.add_fp_page)
        self.gridLayout_8.setObjectName("gridLayout_8")
        # add filepath label
        self.label_7 = QtWidgets.QLabel(self.add_fp_page)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.add_fp_page)
        
        # --------------------add filepath page end--------------------

        # grid layout of content page
        self.gridLayout_7 = QtWidgets.QGridLayout(self.content_page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.addWidget(self.stackedWidget, 0, 0, 1, 1)


        # --------------------content page widget end--------------------


        # grid layout of central widget
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        # header widget in grid layout of central widget
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        # sidebar widget in grid layout of central widget
        self.gridLayout.addWidget(self.sidebar, 1, 0, 1, 1)
        # content page widget in grid layour of central widget
        self.gridLayout.addWidget(self.content_page, 1, 1, 1, 1)

        # central widget in mainwindow
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        self.close_btn.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fr_label.setText(_translate("MainWindow", "FACE RECOGNIZER"))
        self.home_btn.setText(_translate("MainWindow", "HOME"))
        self.add_data_btn.setText(_translate("MainWindow", "ADD DATA"))
        self.recg_face_btn.setText(_translate("MainWindow", "RECOGNIZE FACE"))
        self.sett_panel_btn.setText(_translate("MainWindow", "SETTINGS PANEL"))
        self.add_camera_btn.setText(_translate("MainWindow", "ADD CAMERA"))
        self.test_video_btn.setText(_translate("MainWindow", "ADD FILEPATH"))
        self.close_btn.setText(_translate("MainWindow", "CLOSE"))
        self.home_page_label.setText(_translate("MainWindow", "STREAM"))
        self.label_3.setText(_translate("MainWindow", "ADD DATA"))
        self.label_4.setText(_translate("MainWindow", "RECOGNIZE FACE"))
        
        self.sett_panel_label.setText(_translate("MainWindow", "SETTINGS PANEL"))
        self.detection_model_label.setText(_translate("MainWindow", "CHOOSE DETECTION MODEL"))
        self.recognition_model_label.setText(_translate("MainWindow", "CHOOSE RECOGNITION MODEL"))
        self.processors_label.setText(_translate("MainWindow", "CHOOSE PROCESSORS"))
        self.save_sett_btn.setText(_translate("MainWindow", "SAVE"))

        self.label_6.setText(_translate("MainWindow", "ADD CAMERA"))
        self.label_7.setText(_translate("MainWindow", "ADD FILEPATH"))

    # def foo(self):


import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
