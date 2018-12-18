
import cv2
import operator
import numpy as np
from PIL import Image

def VideoOverlay(frame, frame2, im_width):


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img1 = Image.fromarray(frame)

    img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
    img2 = Image.fromarray(img2)
    img2.thumbnail((200, 200), Image.ANTIALIAS)

    # suppose img2 is to be shifted by `shift` amount
    # shift = (int(im_width) - 300 , int(im_height) - 80)
    shift = (int(im_width) + 5, 0)

    # compute the size of the panorama
    nw, nh = map(max, map(operator.add, img2.size, shift), img1.size)

    # paste img1 on top of img2
    newimg1 = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
    newimg1.paste(img2, shift)
    newimg1.paste(img1, (0, 0))

    # paste img2 on top of img1
    newimg2 = Image.new('RGBA', size=(nw, nh), color=(0, 0, 0, 0))
    newimg2.paste(img1, (0, 0))
    newimg2.paste(img2, shift)

    # blend with alpha=0.5
    frame = Image.blend(newimg1, newimg2, alpha=0.4)
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    return frame

def EmtionBarGraph():

    cam = cv2.VideoCapture('test.mp4')
    im_width = cam.get(3)
    im_height = cam.get(4)

    while True:

        ret, frame = cam.read()

        frame = VideoOverlay(frame, frame.copy(), im_width)



        cv2.imshow('Emo', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    EmtionBarGraph()


