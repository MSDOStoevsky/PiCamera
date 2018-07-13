import os
import cv2
import imutils
import datetime

def start_camera(id):

    frsize = 500
    initial_frame = None

    cv2.namedWindow("Camera")
    vcap = cv2.VideoCapture( (id-1) )

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    vwrite = cv2.VideoWriter('output.avi',fourcc, 20.0, (480, 640))

    while vcap.isOpened():
        frame = vcap.read()[1]
        if frame is None:
            break
        text = "Unoccupied"

        frame = cv2.transpose(frame, -90)
        frame = cv2.flip(frame,-1)
        frame = cv2.flip(frame,1)
        vwrite.write(frame)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if initial_frame is None:
            initial_frame = gray
            continue
        
        frame_delta = cv2.absdiff(initial_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        for c in cnts:
            if cv2.contourArea(c) < frsize:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Occupied"

        cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		    (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)


        cv2.imshow("Camera", frame)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    vs.release()
    vout.release()
    cv2.destroyWindow("Camera")

def dependency_path():
    print(os.path.abspath(cv2.__file__))

def terminate():
    print("removing all nodes")
    cv2.destroyAllWindows()