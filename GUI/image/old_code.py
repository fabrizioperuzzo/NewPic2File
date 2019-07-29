        def mouse_crop(event, x, y, flags, param):

            global self.x_start, self.y_start, self.x_end, self.y_end, cropping, image

            refPoint = []

            if event == cv2.EVENT_LBUTTONDOWN:
                if cropping == False:
                    self.x_end, self.y_end = x, y
                    cropping = True

                if event == cv2.EVENT_MOUSEMOVE:
                    if cropping == True:
                        self.x_end, self.y_end = x, y

                        # if the left mouse button was released
                        if event == cv2.EVENT_LBUTTONUP:
                            # record the ending (x, y) coordinates
                            self.x_end, self.y_end = x, y
                            cropping = False  # cropping is finished

                            refPoint = [(x_start, self.y_start), (x_end, self.y_end)]

                            if len(refPoint) == 2:  # when two points were found
                                image = image[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]


        mouse_crop

        cv2.imshow("Cropped", image)
        cv2.waitKey(0)


    Inizia()

    def draw_point(event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDBLCLK:
            cv2.circle(image, (x, y), 2, (255, 255, 255), 1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            strxy = str(x) + ',' + str(y)
            cv2.putText(image, strxy, (x + 5, y), font, 0.4, (255, 255, 255), 1)
            cv2.imshow("image", image)
            print(x, y)
            ls_point.append([x, y])


    while True:


        cv2.namedWindow("image")
        cv2.setMouseCallback("image", draw_point)
        cv2.imshow("image", image)


        if cv2.waitKey(1) & 0xFF == ord("q"):
            print "\nLe coordinate degli assi sono:", ls_point[:3]
            print "\nLa lista di punti e':\n", ls_point[3:]
            break

    cv2.destroyAllWindows()


Inizia()


  import numpy as np
import cv2
import os
import pyautogui
import imutils
import datetime


currentDT = str(datetime.datetime.now())
currentDT = currentDT.replace(' ', '_').replace(':', '').replace('-', '')
currentDT = currentDT.split('.')[0]
filename = "image\\" + str(currentDT) + '.png'
print (filename)

imgss = pyautogui.screenshot()
imgss = cv2.cvtColor(np.array(imgss), cv2.COLOR_RGB2BGR)
imgss = cv2.imwrite(filename, imgss)
image = cv2.imread(filename)

refPt = []
ls_point = []
cropping = False
axis_on = True



def draw_line(event,x,y,flags,param):
    global refPt, cropping, axis_on

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)
        cropping = False
        axis_on = False


def draw_point(event,x,y,flags,param):
    global ls_point
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x,y), 2, (255,255,255), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strxy = str(x)+ ',' + str(y)
        cv2.putText(image, strxy, (x+5,y), font, 0.4, (255,255,255),1)
        cv2.imshow("image", image)
        print(x,y)
        ls_point.append([x,y])


while True:

    if axis_on == True:
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", draw_line)
        cv2.imshow("image",image)

    elif axis_on == False:
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", draw_point)
        cv2.imshow("image", image)

    if cv2.waitKey(1) & 0xFF == ord("r"):
        refPt = []
        ls_point = []
        cropping = False
        axis_on = True

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print "\nLe coordinate degli assi sono:\n", refPt
        print "\nLa lista di punti e':\n",ls_point
        break

cv2.destroyAllWindows()

