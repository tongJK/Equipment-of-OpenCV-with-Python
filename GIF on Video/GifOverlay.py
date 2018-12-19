
import os
import cv2
from time import sleep
import numpy as np
from PIL import Image, ImageEnhance, ImageSequence

def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))

    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, (int((im.size[0] - w) / 2), int((im.size[1] - h) / 2)))
    else:
        layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)

def GIFCreator(inGif):

    im = Image.open(inGif)

    index = 1
    for frame in ImageSequence.Iterator(im):
        frame.save("XXX%d.png" % index)
        index += 1


def WarningGIG(frame, path,  im_width, im_height, overlayw, overlayh):


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img1 = Image.fromarray(frame)
    img2 = Image.open(path)
    img2.thumbnail((im_width, im_height) , Image.ANTIALIAS)

    frame = watermark(img1, img2, (overlayw, overlayh), 0.5)
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    return frame

def VideoOverlay(frame, im_width, im_height, overlayw, overlayh):


    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img1 = Image.fromarray(frame)
    img2 = Image.open('DECEPTION 1.png')
    img2.thumbnail((im_width, im_height) , Image.ANTIALIAS)

    frame = watermark(img1, img2, (overlayw, overlayh), 0.5)
    frame = np.array(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    return frame

if __name__ == '__main__':

    cam = cv2.VideoCapture('test.mp4')
    im_width = cam.get(3)
    im_height = cam.get(4)

    i = 0
    round = 0

    while True:
        _, frame = cam.read()

        if round <= 70:
            try:
                path = 'frame%s.png' % str(i + 1)
                frame = WarningGIG(frame, path, 800, 600, 600, int(im_height/2) - 100)
                sleep(.1)

            except:
                i = 0
                round += 1

        i += 1

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cv2.destroyAllWindows()
    cam.release()


