import sys #for system commands like open/save dialog
import os #for system detection
import cv2  # Image proc.
import numpy as np #for working with arrays
import matplotlib.patches as mpatches #histograms
import pytesseract  # OCR
from matplotlib import pyplot as plt #histograms
from PIL import Image #Image Processing
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets
from skimage.filters import threshold_yen
from skimage.exposure import rescale_intensity
from PyQt5.QtWidgets import QMessageBox
from test import * #imports the ui pytHon file

class MainWindow(QtWidgets.QMainWindow):
    print(os.name) #prints out system name
    if os.name == "nt": print("Windows System")
    if os.name == "posix": print("MAC-OS")
    def __init__(self):
        QtWidgets.QWidget.__init__(self) #UI init and set-up
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.menuBar.setNativeMenuBar(0) #fix for mac menubar issue
        #define elements for further use
        self.text = ui.textEdit
        self.inputImg = ui.input
        self.inputIcon = ui.AddPic
        self.TextIcon = ui.label_2
        self.radioLAT = ui.radioButton
        self.radioENG = ui.radioButton_2
        self.fontSize = ui.spinBox
        self.histogram = ui.histogram_window
        ###############################################
        #########  Open/Save/OCR buttons   ############
        ###############################################
        # Extract text with pytesseract (OCR)
        extract_btn = ui.extract_Text
        if os.name == "nt": extract_btn.setShortcut("Ctrl+E")
        if os.name == "posix": extract_btn.setShortcut("Cmd+E")
        extract_btn.clicked.connect(self.extract_text)
        # Open image
        open_btn = ui.actionOpen_Image
        if os.name == "nt": open_btn.setShortcut("Ctrl+O")
        if os.name == "posix": open_btn.setShortcut("Cmd+O")
        # Open image with menu bar
        menu_open_btn = ui.actionOpen_Image
        menu_open_btn.triggered.connect(self.openImage)
        menu_open_btn.triggered.connect(self.laplacian_test)
        menu_open_btn.triggered.connect(self.autorotate)
        menu_open_btn.triggered.connect(self.automatic_brightness_and_contrast)
        menu_open_btn.triggered.connect(self.noise_reduction)
        #menu_open_btn.triggered.connect(self.remove_background)
        # Save edited image
        save_img_btn = ui.actionSave_Image
        if os.name == "nt": save_img_btn.setShortcut("Ctrl+S")
        if os.name == "posix": save_img_btn.setShortcut("Cmd+S")
        save_img_btn.triggered.connect(self.saveImage)
        # Connects to the shortcut display
        menu_shortcut_btn = ui.actionShortcuts
        menu_shortcut_btn.triggered.connect(self.shortcuts)
        # Clear the text window
        clear_text_btn = ui.clear_text_btn
        clear_text_btn.clicked.connect(self.clearText)
        # Save text to new file
        menu_save_text_btn = ui.actionSave_Text_To_File
        menu_save_text_btn.triggered.connect(self.saveText)
        ########################################
        #########  Image Processing   ##########
        ########################################
        # Edge_detect
        edge_detect_menu_btn = ui.actionEdge_Detect
        edge_detect_menu_btn.triggered.connect(self.edge_detect)
        # Segmentation
        segmentation_menu_btn = ui.actionSegmentation
        segmentation_menu_btn.triggered.connect(self.segmentation)
        # Contrast test
        contrast_menu_btn = ui.actionContrast_Test
        contrast_menu_btn.triggered.connect(self.automatic_brightness_and_contrast)
        # Noise reduction
        noise_menu_btn = ui.actionNoise_Reduction
        noise_menu_btn.triggered.connect(self.noise_reduction)
        # Erode text
        erode_menu_btn = ui.actionErode
        erode_menu_btn.triggered.connect(self.erode)
        # Tool tip information
        ui.input.setToolTip('Select an image to convert')
        ui.textEdit.setToolTip('Image output')
        # Remove background
        bckg_rem_menu_btn = ui.actionRemove_Background
        bckg_rem_menu_btn.triggered.connect(self.remove_background)
        # Timer progress bar thing
        self.pbar = ui.progressBar
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
    ####################################################################################################################
        # Image rotation
    def autorotate(self):  # pagriez ieladeto attelu
        image = cv2.imread('res/temp_edit.png')
        self.inputIcon.setVisible(0)  # hides the addpic icon # convert the image to grayscale and flip the foreground
        # and background to ensure foreground is now "white" and # the background is "black"
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.bitwise_not(gray)
        cv2.imshow("gray", gray)
        # threshold the image, setting all foreground pixels to  # 255 and all background pixels to 0
        thresh = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cv2.imshow("thresh", thresh)
        # grab the (x, y) coordinates of all pixel values that # are greater than zero, then use these coordinates to
        # compute a rotated bounding box that contains all  # coordinates
        coords = np.column_stack(np.where(thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]
        # the `cv2.minAreaRect` function returns values in the # range [-90, 0); as the rectangle rotates clockwise the
        # returned angle trends to 0 -- in this special case we # need to add 90 degrees to the angle
        if angle < -45:
            angle = -(90 + angle)
        # otherwise, just take the inverse of the angle to make  # it positive
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h),
                                 flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        # draw the correction angle on the image so we can validate it  # cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle),
        #           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) # show the output image
        print("[Rotate] Source Image Angle Turned By: {:.3f}".format(angle))
        cv2.imwrite('res/temp_edit.png', rotated)
        label = self.inputImg
        pixmap = QtGui.QPixmap('res/temp_edit.png')
        pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap_resized)
    ####################################################################################################################
        # Automatic brightness and contrast optimization with optional histogram clipping
    def automatic_brightness_and_contrast(self, clip_hist_percent=1):
        try:
            image = cv2.imread('res/temp_edit.png')
            label = self.inputImg
            self.inputIcon.setVisible(0)  # hides the addpic icon
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Calculates grayscale histogram from picture (blue)
            hist = cv2.calcHist([gray], [0], None, [256], [0, 256])  # image, channels, mask, hist size, ranges
            hist_size = len(hist)
            # Calculate cumulative distribution from the histogram ->
            # Lai noteiktu kur krāsas frekvence ir mazāka par sliekšņa vērtību un nogrieztu labo un kreiso pusi, dodot min un max diapazonu.
            accumulator = []
            accumulator.append(float(hist[0]))  # append -> adds an item to the end of the list (self, object)
            for index in range(1, hist_size):
                accumulator.append(accumulator[index - 1] + float(
                    hist[index]))  # finds the given element in a list and returns its position
            # Izgriešanas metode noņem visattālākās detaļas un palielina kontrastu/spilgtumu
            # Locate points to clip
            maximum = accumulator[-1]
            clip_hist_percent *= (maximum / 100.0)
            clip_hist_percent /= 2.0
            # Locate left cut
            minimum_gray = 0
            while accumulator[minimum_gray] < clip_hist_percent:
                minimum_gray += 1
            # Locate right cut
            maximum_gray = hist_size - 1
            while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
                maximum_gray -= 1
            # Calculate alpha and beta values
            # alpha=2 #Contrast, #beta=1 #Brightness
            # Alpha = min and max grayscale range (diapazons) after clipping and divide it from output range of 255
            alpha = 255 / maximum_gray - minimum_gray
            beta = -minimum_gray * alpha
            # ConvertScaleAbs -> scales (mērogo), calculates absolute values and converts the result to 8-bit
            auto_result = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
            print("[Contrast] Image Alpha Value : {:.3f}".format(alpha))
            print("[Contrast] Image Beta Value: {:.3f}".format(beta))
            cv2.imwrite('res/temp_edit.png', auto_result)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            # New histogram - visualisation after clipping (orange)
            new_hist = cv2.calcHist([gray], [0], None, [256],
                                    [minimum_gray, maximum_gray])  # image, channels, mask, hist size, ranges
            plt.plot(hist)
            plt.plot(new_hist)
            plt.xlim([0, 256])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(), hst_label.height(), QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)

        except:
            print("An exception occurred")
    ####################################################################################################################
    # Image sharpening
    def sharpen(self):
        try:
            image = cv2.imread('res/temp_edit.png')
            kernel_sharpening = np.array([[-1, -1, -1],
                                          [-1, 9, -1],
                                          [-1, -1, -1]])
            sharpened = cv2.filter2D(image, -1, kernel_sharpening)
            cv2.imwrite('res/temp_edit.png', sharpened)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(), hst_label.height(), QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
    ####################################################################################################################
        # Image noise reduction
    def noise_reduction(self):
        try:
            image = cv2.imread('res/temp_edit.png')
            # Sobel gradient
            # Computes gradients along the X and Y axis, respectively
            sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
            sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
            sobelX = np.uint8(np.absolute(sobelX))
            sobelY = np.uint8(np.absolute(sobelY))
            sobelCombined = cv2.bitwise_or(sobelX, sobelY)
            # If image histogram = 0 -> blur
            if plt.hist(image.ravel(), 1, [0, 0]):
                b,g,r=cv2.split(image)#get b, g, r
                rgb_img=cv2.merge([r,g,b])#switch it to rgb
                dst=cv2.fastNlMeansDenoisingColored(rgb_img,None,10,10,7,21)
                cv2.imwrite('res/temp_edit.png', dst)
            else:
                cv2.imwrite('res/temp_edit.png', sobelCombined)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='ImageHistogram')
            plt.xlabel('RGBChannelValues')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(), hst_label.height(), QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
    ###########################################################################################################
        # Laplacian filter blur detection
    def laplacian_test(self):
        try:
            def variance_of_laplacian(image):
                 return cv2.Laplacian(image, cv2.CV_64F).var()
            threshold = 100.0
            image = cv2.imread('res/temp_edit.png')
            #ALREADY DONE IN AUTO-CONTRAST SO NOT NEEDED: gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = variance_of_laplacian(image)
            if fm < threshold:
                text = "Blurry"
            if fm > threshold:
                text = "Not Blurry"
            cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            print("[Blur Detection Result] Selected Image is:  " + text)
            print("[Blur Detection Result] Image Blurr value : {:.3f}".format(fm))

            if text == "Blurry": #if picture is blurry -> sharpen it
                self.sharpen()
        except:
            print("An exception occurred")
    ####################################################################################################################
        # Image background removal
    def remove_background(self):
        try:
            image = cv2.imread('res/temp_edit.png')
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)

            yen_threshold = threshold_yen(image)
            bright = rescale_intensity(image, (0, yen_threshold), (0, 255))

            cv2.imwrite('res/temp_edit.png', bright)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
        ####################################################################################################################
        # Text eroder
    def erode(self):  # erode text
        try:
            img = cv2.imread('res/temp_edit.png')
            label = self.inputImg
            self.inputIcon.setVisible(0)  # hides the addpic icon
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            kernel = np.ones((3, 3), np.uint8)  # how strong errode is
            kernel_sharpening = np.array(
                [[-1, -1, -1],
                 [-1, 9, -1],
                 [-1, -1, -1]])
            sharpened = cv2.filter2D(img, -1, kernel_sharpening)
            median = cv2.medianBlur(sharpened,3)
            eroded = cv2.erode(median, kernel, iterations=1)
            dilated = cv2.dilate(eroded, kernel, iterations=1)
            cv2.imwrite('res/temp_edit.png', dilated)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            # izveido histogrammu un parada
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(), hst_label.height(), QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
    ####################################################################################################################
    #Open Image using AUTO rotate/contrast/blur detection+sharpen if needed/remove background:
    ####################################################################################################################
        # Open image
    def openImage(self):
        try:
            fileName, _ = QFileDialog.getOpenFileName(self, "Select An Image To Open", "",
                                                          "All Files (*);;PNG Files (*.png);; JPG Files (*.jpg)")
            f = open(fileName, "r")
            print("---------------------------------------------------------------------------------------------------")
            print("[Image] Image opened:  " + fileName)
            label = self.inputImg
            self.inputIcon.setVisible(0)  # hides the addpic icon
            image = cv2.imread(fileName)
            cv2.imwrite('res/temp_edit.png', image)
            pixmap = QtGui.QPixmap(fileName)
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(),hst_label.height(),QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
            #based on theory previously discussed, the image processing part of the project should have:
                #contrast control
                #noise detection and lessening
                #auto-rotate
                #blur detection and lessening
                #remove background
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("No image selected! Please try to import a new image!")
            msgBox.setWindowTitle("Exception!")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                print('OK clicked')

            print("An exception occurred")
    ####################################################################################################################
    # Incomplete edits
    ####################################################################################################################
    def edgyness_test(self):
        try:
            image = cv2.imread('res/temp_edit.png')
            label = self.inputImg
            self.inputIcon.setVisible(0)  # hides the addpic icon
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            self.inputIcon.setVisible(0)  # hides the addpic icon
            new_img = cv2.Canny(image, 100, 10)
            cv2.imwrite('res/temp_edit.png', new_img)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(), label.height(), QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(), hst_label.height(), QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
    ####################################################################################################################
    def blur(self): #currently in testing mode
        try:
            image = cv2.imread('res/temp_edit.png') # Reading in and displaying our image
            self.inputIcon.setVisible(0)  # hides the addpic icon
            kernel_3x3 = np.ones((3, 3), np.float32) / 9
            blurred = cv2.filter2D(image, -1, kernel_3x3)
            cv2.imwrite('res/temp_edit.png', blurred)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            #pixmap_resized = pixmap.scaled(600, 600, QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(),hst_label.height(),QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
    ####################################################################################################################
    def segmentation(self): #currently in testing mode
        try:
            image = cv2.imread('res/temp_edit.png')
            label = self.inputImg
            self.inputIcon.setVisible(0)  # hides the addpic icon
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            #obligati jabut ieprieks deginetam objektam
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #making it grayscale at first
            _,mask = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)  #segmentation ##izveidot adaptīvo
            cv2.imwrite('res/temp_edit.png', mask)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(),hst_label.height(),QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
        except:
            print("An exception occurred")
    ####################################################################################################################
    def edge_detect(self): #edge detection (NOT AUTO)
        try:
            image = cv2.imread('res/temp_edit.png')
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            new_img = cv2.Canny(image, 0, 200)
            cv2.imwrite('res/temp_edit.png', new_img)
            label = self.inputImg
            pixmap = QtGui.QPixmap('res/temp_edit.png')
            pixmap_resized = pixmap.scaled(label.width(),label.height(),QtCore.Qt.KeepAspectRatio)
            label.setPixmap(pixmap_resized)
            img = cv2.imread('res/temp_edit.png', 0)
            plt.hist(img.ravel(), 256, [0, 256], color="magenta", ec="skyblue");
            hist_data = mpatches.Patch(color='skyblue', label='Image Histogram')
            plt.xlabel('RGB Channel Values')
            plt.ylabel('values')
            plt.legend(handles=[hist_data])
            plt.savefig("histogram_temp.png")
            hst_label = self.histogram
            pixmap = QtGui.QPixmap('histogram_temp.png')
            pixmap_resized = pixmap.scaled(hst_label.width(),hst_label.height(),QtCore.Qt.KeepAspectRatio)
            hst_label.setPixmap(pixmap_resized)
            self.initUI()
        except:
            print("An exception occurred")
    ####################################################################################################################
    #SAVE IMAGE AND TEXT
    ####################################################################################################################
    def saveText(self): #save output text
        try:
            fileName = QFileDialog.getSaveFileName(self, "Save Text", "",
                                                "All Files (*);;TEXT Files (*.txt)")
            with open(fileName[0], 'w') as f:
                my_text = self.text.toPlainText()
                f.write(my_text)
        except:
            print("An exception occurred")
    ####################################################################################################################
    def saveImage(self):  # ⚠under construction⚠️
        try:
            fileName = QFileDialog.getSaveFileName(self, "Select Where To Save The Edited Image",'',
                                                        "*.png")
            image = cv2.imread(fileName)

            with open(fileName[0], 'w') as f:
                image = 'res/temp_edit.png'
                f.write(image)
        except:
            print("An exception occurred")
    ####################################################################################################################
    def clearText(self):  # clear the output window
        self.text.clear()
        print("[Text cleared]")
    ####################################################################################################################
    def handleTimer(self):
        value = self.pbar.value()
        self.pbar.setValue(100)
    ####################################################################################################################
    def shortcuts(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("WINDOWS:\n"
                       "-----------------------\n"
                       "Ctrl + O - Open Image\n"
                       " Ctrl + S - Save Image\n"
                       " Ctrl + E - Extract Text From Image\n\n"
                       "MAC-OS:\n"
                       "-----------------------\n"
                       " Cmd + O - Open Image\n"
                       " Cmd + S - Save Image\n"
                       " Cmd + E - Extract Text From Image\n")
        msgBox.setWindowTitle("Shortcut Information:")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
    ####################################################################################################################
    def extract_text(self):
        try:
            #make sure the directory points to the place where tesseract is
            #WINDOWS:
            if os.name =='nt':
                pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract'
            #MAC-OS:
            if os.name == 'posix':
                pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR-Mac/tesseract'  # '/usr/local/bin/tesseract'

            img = Image.open('res/temp_edit.png') #open temp image
            if self.radioENG.isChecked():
                text = pytesseract.image_to_string(img, lang='eng+rus+lav') # izmanto anglu valodu
            else:
                text = pytesseract.image_to_string(img, lang='lav')  # izmanto latviesu valodu
            self.TextIcon.setVisible(0)
            self.text.setText(text)
            self.biggerText()
            self.handleTimer()
        except:
            print("An exception occurred")
  ####################################################################################################################
    def biggerText(self):  # the concept needs a lot of work
        self.fontSize.valueChanged(self.text.setFontPointSize(self.fontSize.value()))
        print("[Font size] {:.3f}".format(self.fontSize.value()))
  ####################################################################################################################
def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
 #opens and shows the main app window
if __name__ == "__main__":
     main()
