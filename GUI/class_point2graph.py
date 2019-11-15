import numpy as np
import cv2
import os
import pyautogui
import Tkinter as tk
import tkMessageBox


class point2graph:

    def __init__(self):

        self.filename = "image\\screenshot.png"
        self.filename_temp = "image\\temp_image.png"
        self.filename_init = "image\\init_image.png"
        self.image = cv2.imread(self.filename)
        self.image_temp = cv2.imread(self.filename)
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
        self.delistance = False
        self.xcoorigwin = float(10.01)
        self.ycoorigwin = float(5.02)
        self.xcoowin = float(45.5)
        self.ycoowin = float(35.6)

    def print_screen(self):

        imgss = pyautogui.screenshot()
        imgss = cv2.cvtColor(np.array(imgss), cv2.COLOR_RGB2BGR)
        imgss = cv2.imwrite(self.filename, imgss)
        self.image = cv2.imread(self.filename)

    def crop_image(self):

        self.image = cv2.imread(self.filename)
        cropping = False

        def mouse_crop(event, x, y, flags, param):

            refPoint = []
            cropping = False

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
                    imgss_init = cv2.imwrite(self.filename_init, self.image)

        while True:

            cv2.namedWindow("image")
            cv2.setMouseCallback("image", mouse_crop)
            cv2.imshow("image", self.image)
            if cv2.waitKey(1) & self.cropped == True:
                break
        cv2.destroyAllWindows()

    def reinitialize(self):
        self.ls_point = []
        print "The list has been reinitialized"
        self.image = cv2.imread(self.filename_init)
        self.delistance = False
        self.cropped = False

    def get_point(self):

        self.image = cv2.imread(self.filename_init)

        def callback():
            midIQ.destroy()

        def draw_point(event, x, y, flags, param):

            def read_label():

                try:

                    f = open("SETTINGS\\label_input.txt", 'r')
                    with f:
                        ls_label = f.readlines()

                    for i in ls_label:
                        ls_label[ls_label.index(i)] = i.replace('\n', '')

                    x0_in = ls_label[4]
                    y0_in = ls_label[5]
                    coomaxX = ls_label[6]
                    coomaxY = ls_label[7]

                except:  # se non trova il file con input .txt

                    x0_in = 0
                    y0_in = 0
                    coomaxX = 10  # coord max X
                    coomaxY = 10  # coord max Y

                return x0_in, y0_in, coomaxX, coomaxY





            if event == cv2.EVENT_LBUTTONDBLCLK:
                imgss_temp = cv2.imwrite(self.filename_temp, self.image)
                cv2.circle(self.image, (x, y), 2, (0, 0, 238), 1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                strxy = str(x) + ',' + str(y)
                cv2.putText(self.image, strxy, (x + 5, y), font, 0.4, (0, 0, 238), 1)
                cv2.imshow("image", self.image)
                print(x, y)
                self.ls_point.append([x, y])
                self.n_click = len(self.ls_point)

                if self.n_click == 1:
                    self.delistance = True

                #         midIQ = tk.Tk()
                #         midIQ.wm_title("Origin-Point")
                #         #
                #         label = tk.Label(midIQ, text="Insert projectname")
                #         label.pack(side="top", fill="x", pady=10)
                #         e20 = tk.Entry(midIQ)
                #         e20.insert(projectname)
                #         e20.pack()
                #         e20.focus_set()
                #         #
                #         label00 = tk.Label(midIQ, text="Insert x,y orgin coordinates")
                #         label00.pack(side="top", fill="x", pady=10)
                #         e21 = tk.Entry(midIQ)
                #         e21.insert(read_label[0], read_label[1])
                #         e21.pack()
                #         e21.focus_set()
                #         b = tk.Button(midIQ, text="Submit", width=10, command=callback)
                #         b.pack()
                #         label0 = tk.Label(midIQ, text="Next step select Y point")
                #         label0.pack(side="top", fill="x", pady=10)
                #         tk.mainloop()
                #         self.delistance = True
                #
                #         self.projname = str(e20.get())
                #         self.xcoorigwin = float(e21.get()[0])
                #         self.ycoorigwin = float(e21.get()[0])
                #






            elif event == cv2.EVENT_RBUTTONDOWN:
                if self.delistance == True:
                    self.ls_point.pop()
                    self.n_click = len(self.ls_point)
                    print self.ls_point
                    self.image = cv2.imread(self.filename_temp)
                    cv2.imshow("image", self.image)
                    self.delistance = False
                elif self.delistance == False:
                    MsgBox = tkMessageBox.askquestion("Warning",
                                                      "Cannot Redo more than one instance\nDo you want to reinitialize all?",
                                                      icon='warning')
                    if MsgBox == 'yes':
                        self.ls_point = []
                        print 'You pressed yes'
                        print "The list has been reinitialized"
                        self.image = cv2.imread(self.filename_init)
                        cv2.imshow("image", self.image)
                        self.delistance = False
                    else:
                        self.delistance = True
                        print 'You pressed no'

        if len(self.ls_point) == 0: tkMessageBox.showinfo("Message",
                                                          "SELECT:\n"
                                                          "1) ORIGIN\n   "
                                                          "2) MAX Y AXIS\n   "
                                                          "3) MAX X AXIS\n   "
                                                          "4) POINTS ON THE GRAPH\n   "
                                                          "5) PRESS ESC TO FINISH\n   "
                                                          "\n"
                                                          "*** MOUSE RIGHT CLICK TO CORRECT WRONG ENTRY ***")

        while True:

            labelwindow = "image"

            cv2.namedWindow(labelwindow)
            cv2.setMouseCallback("image", draw_point)
            cv2.imshow(labelwindow, self.image)

            if cv2.waitKey(33) == ord('i'):

                self.ls_point = []
                print "The list has been reinitialized"
                self.image = cv2.imread(self.filename_init)
                cv2.imshow("image", self.image)
                self.delistance = False

            k = cv2.waitKey(33)
            if k == 27:
                print "\nThe list of point is e':\n", self.ls_point
                tkMessageBox.showinfo("Message", "Now press Print Coordinate from File/Menu ")
                break

        cv2.destroyAllWindows()
