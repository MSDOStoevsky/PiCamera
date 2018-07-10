import os
import cv2

__VC = None

def start_camera():
    cv2.namedWindow("preview")
    __VC = cv2.VideoCapture(0)

    if __VC.isOpened(): # try to get the first frame
        rval, frame = __VC.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = __VC.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            stop_camera()
            break

def stop_camera():

    if os.name == 'nt':
        __VC.release()
    cv2.destroyWindow("preview")