
import cv2

import dlib
from imutils import face_utils

def DasedLine(frame, p1, p2):

    # cv2.rectangle(frame, p1, p2, (0, 0, 255), 3)

    dd = 0
    dash_space = 30
    dash_long = 10

    if p1[0] < p2[0]:
        for i in range(int(p1[0]), int(p2[0]), int(p2[0])//dash_space):

            if dd == 0:
                cv2.line(frame, (i, p1[1]), (i + dash_long, p1[1]), (0, 0, 255), 2)
                cv2.line(frame, (i, p2[1]), (i + dash_long, p2[1]), (0, 0, 255), 2)
                dd = 1

            else:
                dd = 0

    else:
        for i in range(int(p2[0]), int(p1[0]), int(p1[0])//dash_space):

            if dd == 0:
                cv2.line(frame, (i, p1[1]), (i + dash_long, p1[1]), (0, 0, 255), 2)
                cv2.line(frame, (i, p2[1]), (i + dash_long, p2[1]), (0, 0, 255), 2)
                dd = 1

            else:
                dd = 0


    if p1[1] < p2[1]:
        for i in range(int(p1[1]), int(p2[1]), int(p2[1])//dash_space):

            if dd == 0:
                cv2.line(frame, (p1[0], i), (p1[0], i + dash_long), (0, 255, 255), 2)
                cv2.line(frame, (p2[0], i), (p2[0], i + dash_long), (0, 255, 255), 2)
                dd = 1

            else:
                dd = 0

    else:
        for i in range(int(p2[1]), int(p1[1]), int(p1[1])//dash_space):

            if dd == 0:
                cv2.line(frame, (p1[0], i), (p1[0], i + dash_long), (0, 255, 255), 2)
                cv2.line(frame, (p2[0], i), (p2[0], i + dash_long), (0, 255, 255), 2)

                dd = 1

            else:
                dd = 0

    return frame

if __name__ == '__main__':

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


    cam = cv2.VideoCapture('Bill_Gates.mp4')
    # cam = cv2.VideoCapture('test.mp4')
    im_width = cam.get(3)
    im_height = cam.get(4)

    while True:
        _, frame = cam.read()

        # frame = imutils.resize(frame, width=800)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        faces = detector(gray, 0)

        for i, face in enumerate(faces):
            # print("Lie_Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            #     i, face.left(), face.top(), face.right(), face.bottom()))
            x_reg, y_reg, w_reg, h_reg = face.left(), face.top(), face.right(), face.bottom()
            # crop_img = frame[y:y + h, x:x + w]
            crop_img = frame[y_reg:h_reg, x_reg:w_reg]

            print('x : {} | y : {}'.format(x_reg, y_reg))
            print('w : {} | h : {}'.format(w_reg, h_reg))
            # print('w : {} | h : {}'.format(int(x_reg) + int(w_reg), int(y_reg) + int(h_reg)))
            frame = DasedLine(frame, (x_reg, y_reg), (int(w_reg), int(h_reg)))
            # cv2.rectangle(frame, (x_reg, y_reg), (w_reg, h_reg), (0, 255, 0), 4)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    cam.release()