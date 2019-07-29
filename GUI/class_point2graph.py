import numpy as np
import cv2
import os
import pyautogui
import Tkinter
import tkMessageBox


class point2graph:

    def __init__(self):

        self.filename = "image\\screenshot.png"
        self.image = cv2.imread(self.filename)
        self.refPt = []
        self.ls_point = []
        self.cropping = False
        self.axis_on = True
        self.ls_point = []
        self.x_start = 0
        self.y_start = 0
        self.x_end = 0
        self.y_end = 0
        self.cropped = False
        
    def print_screen(self):
        
        imgss = pyautogui.screenshot()
        imgss = cv2.cvtColor(np.array(imgss), cv2.COLOR_RGB2BGR)
        imgss = cv2.imwrite(self.filename, imgss)
        self.image = cv2.imread(self.filename)

    def crop_image(self):

        def mouse_crop(event, x, y, flags, param):
            cropping = False
            refPoint = []

            if event == cv2.EVENT_LBUTTONDOWN:
                if cropping == False:
                    self.x_start, self.y_start, self.x_end, self.y_end = x, y, x, y
                    cropping = True
            elif event == cv2.EVENT_MOUSEMOVE:
                if cropping == True:
                    self.x_end, self.y_end = x, y
                    # if the left mouse button was released
            elif event == cv2.EVENT_LBUTTONUP:
                # record the ending (x, y) coordinates
                self.x_end, self.y_end = x, y
                cropping = False  # cropping is finished
                refPoint = [(self.x_start, self.y_start), (self.x_end, self.y_end)]
                if len(refPoint) == 2:  # when two points were found
                    self.image = self.image[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
                    self.cropped = True

        while True:

            cv2.namedWindow("image")
            cv2.setMouseCallback("image", mouse_crop)
            cv2.imshow("image", self.image)
            if cv2.waitKey(1) & self.cropped == True:
                break
        cv2.destroyAllWindows()
            



    def get_point(self):

        def draw_point(event, x, y, flags, param):

            if event == cv2.EVENT_LBUTTONDBLCLK:
                cv2.circle(self.image, (x, y), 2, (0, 0, 238), 1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                strxy = str(x) + ',' + str(y)
                cv2.putText(self.image, strxy, (x + 5, y), font, 0.4, (0, 0, 238), 1)
                cv2.imshow("image", self.image)
                print(x, y)
                self.ls_point.append([x,y])

        if len(self.ls_point) == 0: tkMessageBox.showinfo("Message", "SELECT IN THE ORDER:\n  \n   1) ORIGIN POINT\n   2) POINT ON Y AXIS\n   3) POINT ON X AXIS\n   4) POINTS OF THE GRAPH\n   \nPRESS ESC TO SAVE DATA")

        while True:

            cv2.namedWindow("image")
            cv2.setMouseCallback("image", draw_point)
            cv2.imshow("image", self.image)

            
            #if cv2.waitKey(1) &  0xFF == ord("q"):
            k = cv2.waitKey(33)
            if k==27:

                print "\nLa lista di punti e':\n", self.ls_point
                tkMessageBox.showinfo("Message", "Now press Print Coordinate from File/Menu ")
                break

        cv2.destroyAllWindows()
