import cv2
import numpy as np
import pyautogui
import time
from pynput.keyboard import Listener
import os

def shoot_screen(key):

    if key.char == "q":

        print("Debug Listener")


        screen_shoot = pyautogui.screenshot()

        file_name = str(time.time_ns()) + ".png"

        file_path = os.path.join('path what you will save the screen shot', file_name)

        screen_shoot.save(file_path)

        image = cv2.imread(file_path)


        output = image.copy()
   
        #find circles with Hough method which is define center position and get radius
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 3,
                                   param1=110, param2=30,
                                   minRadius=15, maxRadius=250)
        print(circles)
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(output, center, 1, (0, 0, 255), 3)
                # circle outline
                radius = i[2]
                cv2.circle(output, center, radius, (255, 0, 255), 3)

        cv2.namedWindow("output")
        cv2.moveWindow("output", 0, 0)


        cv2.imshow("output", output )
        cv2.waitKey(200)


        #mouse cursor
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                cX, cY = center

                cX = cX + 10
                cY = cY + 30

                pyautogui.moveTo(cX, cY, duration=1)

        cv2.destroyAllWindows()
        cv2.waitKey(100)

with Listener(on_release=shoot_screen) as listener:
    listener.join()
