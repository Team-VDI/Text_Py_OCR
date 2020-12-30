# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1293, 880)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(47, 37, 37);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(780, 50, 501, 441))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(85, 85, 85);\n"
"font: 75 12pt \"Consolas\";\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.input = QtWidgets.QLabel(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(20, 50, 591, 761))
        self.input.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.input.setLineWidth(3)
        self.input.setText("")
        self.input.setScaledContents(False)
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.label.setObjectName("label")
        self.AddPic = QtWidgets.QLabel(self.centralwidget)
        self.AddPic.setGeometry(QtCore.QRect(230, 370, 131, 131))
        self.AddPic.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.AddPic.setText("")
        self.AddPic.setPixmap(QtGui.QPixmap("res/addPicIcon.png"))
        self.AddPic.setScaledContents(True)
        self.AddPic.setAlignment(QtCore.Qt.AlignCenter)
        self.AddPic.setObjectName("AddPic")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(780, 10, 81, 31))
        self.label_3.setObjectName("label_3")
        self.clear_text_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_text_btn.setGeometry(QtCore.QRect(1090, 490, 191, 21))
        self.clear_text_btn.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.clear_text_btn.setObjectName("clear_text_btn")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(630, 320, 95, 20))
        self.radioButton.setStyleSheet("QRadioButton{\n"
"color:white\n"
"}")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(630, 360, 95, 20))
        self.radioButton_2.setStyleSheet("QRadioButton{\n"
"    color:white\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(930, 210, 191, 101))
        font = QtGui.QFont()
        font.setFamily("HP Simplified")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 290, 141, 16))
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(630, 480, 61, 21))
        self.spinBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.spinBox.setMinimum(12)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 450, 71, 20))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 20, 441, 23))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    color:white;\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(235,150,111);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
"\"\"\"\n"
"\n"
"COMPLETED_STYLE = \"\"\"\n"
"QProgressBar{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: red;\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.histogram_window = QtWidgets.QLabel(self.centralwidget)
        self.histogram_window.setGeometry(QtCore.QRect(780, 530, 501, 281))
        self.histogram_window.setStyleSheet("background-color: rgb(85, 85, 85);")
        self.histogram_window.setText("")
        self.histogram_window.setObjectName("histogram_window")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(780, 499, 111, 31))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 530, 151, 60))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.extract_Text = QtWidgets.QPushButton(self.centralwidget)
        self.extract_Text.setGeometry(QtCore.QRect(620, 210, 151, 60))
        self.extract_Text.setMinimumSize(QtCore.QSize(0, 40))
        self.extract_Text.setStyleSheet("QPushButton{\n"
"    color: rgb(51,51,51);\n"
"    background-color: rgb(235, 150, 111);\n"
"    font-size: 14px;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:white\n"
"}")
        self.extract_Text.setObjectName("extract_Text")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(620, 410, 151, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(620, 180, 151, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(620, 610, 151, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1293, 26))
        self.menuBar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(89, 89, 89);")
        self.menuBar.setObjectName("menuBar")
        self.menuImage = QtWidgets.QMenu(self.menuBar)
        self.menuImage.setObjectName("menuImage")
        self.menuShortcuts = QtWidgets.QMenu(self.menuBar)
        self.menuShortcuts.setObjectName("menuShortcuts")
        self.menuButton_Tests = QtWidgets.QMenu(self.menuBar)
        self.menuButton_Tests.setObjectName("menuButton_Tests")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_Image = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/picture_J3z_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Image.setIcon(icon1)
        self.actionOpen_Image.setObjectName("actionOpen_Image")
        self.actionSave_Image = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("E:/Downloads/Custom Desktop Icons/download_DkF_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Image.setIcon(icon2)
        self.actionSave_Image.setObjectName("actionSave_Image")
        self.actionShortcuts = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("E:/Downloads/Custom Desktop Icons/settings_5P0_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShortcuts.setIcon(icon3)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionSave_Text_To_File = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("E:/Downloads/Custom Desktop Icons/document_Zha_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Text_To_File.setIcon(icon4)
        self.actionSave_Text_To_File.setObjectName("actionSave_Text_To_File")
        self.actionEdge_Detect = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detect.setObjectName("actionEdge_Detect")
        self.actionSegmentation = QtWidgets.QAction(MainWindow)
        self.actionSegmentation.setObjectName("actionSegmentation")
        self.actionContrast_Test = QtWidgets.QAction(MainWindow)
        self.actionContrast_Test.setObjectName("actionContrast_Test")
        self.actionNoise_Reduction = QtWidgets.QAction(MainWindow)
        self.actionNoise_Reduction.setObjectName("actionNoise_Reduction")
        self.actionErode = QtWidgets.QAction(MainWindow)
        self.actionErode.setObjectName("actionErode")
        self.actionRemove_Background = QtWidgets.QAction(MainWindow)
        self.actionRemove_Background.setObjectName("actionRemove_Background")
        self.menuImage.addAction(self.actionOpen_Image)
        self.menuImage.addAction(self.actionSave_Image)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionSave_Text_To_File)
        self.menuShortcuts.addAction(self.actionShortcuts)
        self.menuButton_Tests.addAction(self.actionEdge_Detect)
        self.menuButton_Tests.addAction(self.actionSegmentation)
        self.menuButton_Tests.addAction(self.actionContrast_Test)
        self.menuButton_Tests.addAction(self.actionNoise_Reduction)
        self.menuButton_Tests.addAction(self.actionErode)
        self.menuButton_Tests.addAction(self.actionRemove_Background)
        self.menuBar.addAction(self.menuImage.menuAction())
        self.menuBar.addAction(self.menuShortcuts.menuAction())
        self.menuBar.addAction(self.menuButton_Tests.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Text Recognition Test"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#fffaec;\">Input Image</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; text-decoration: underline; color:#fffaec;\">Output </span></p></body></html>"))
        self.clear_text_btn.setText(_translate("MainWindow", "Clear"))
        self.radioButton.setText(_translate("MainWindow", "Latvian"))
        self.radioButton_2.setText(_translate("MainWindow", "English"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Text</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#dfdace;\">Language selection:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#dfdace;\">Font size:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600; text-decoration: underline; color:#fffaec;\">Histogram</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Refresh Font"))
        self.extract_Text.setText(_translate("MainWindow", "Convert"))
        self.menuImage.setTitle(_translate("MainWindow", "Image"))
        self.menuShortcuts.setTitle(_translate("MainWindow", "Help"))
        self.menuButton_Tests.setTitle(_translate("MainWindow", "Image Tests"))
        self.actionOpen_Image.setText(_translate("MainWindow", "Open Image"))
        self.actionSave_Image.setText(_translate("MainWindow", "Save Image"))
        self.actionShortcuts.setText(_translate("MainWindow", "Shortcuts"))
        self.actionSave_Text_To_File.setText(_translate("MainWindow", "Save Text To File"))
        self.actionEdge_Detect.setText(_translate("MainWindow", "Edge Detect"))
        self.actionSegmentation.setText(_translate("MainWindow", "Segmentation"))
        self.actionContrast_Test.setText(_translate("MainWindow", "Contrast Test"))
        self.actionNoise_Reduction.setText(_translate("MainWindow", "Noise Reduction"))
        self.actionErode.setText(_translate("MainWindow", "Erode"))
        self.actionRemove_Background.setText(_translate("MainWindow", "Remove Background"))
