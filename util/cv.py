import os
import cv2
import logging

def start_camera(id):

    cv2.namedWindow("Camera")
    vs = cv2.VideoCapture( (id-1) )

    vs.set(3, 480)
    vs.set(4, 640)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vout = cv2.VideoWriter('output.avi',fourcc, 20.0, (480, 640))

    while vs.isOpened():
        rval, frame = vs.read()

        if rval == True:
            frame = cv2.transpose(frame, -90)
            frame = cv2.flip(frame,1)
            
            vout.write(frame)
            cv2.imshow("Camera", cv2.flip(frame,-1))
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                break
        else:
            break

    vs.release()
    vout.release()
    cv2.destroyWindow("Camera")

def dependency_path():
    print(os.path.abspath(cv2.__file__))

def terminate():
    print("removing all nodes")
    cv2.destroyAllWindows()