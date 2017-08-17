import cv2 as cv
import numpy as np

def applyCustomColorMap(im_gray):
    lut = np.zeros((256, 1, 3), dtype="uint8")
    for i in xrange(256):
        lut[i, 0, 0] = max(min((127 - i) * 2, 255), 0) if i < 127 else 0
        lut[i, 0, 1] = max(min((i - 127) * 2, 255), 0) if i > 127 else 0
        lut[i, 0, 2] = max(min((127 - i) * 2, 255), 0) if i < 127 else 0

    print lut[:, 0, 0]
    im_color = cv.LUT(im_gray, lut)
    im_falsecolor_r = cv.LUT(im_gray, lut[:, 0, 0])
    im_falsecolor_g = cv.LUT(im_gray, lut[:, 0, 1])
    im_falsecolor_b = cv.LUT(im_gray, lut[:, 0, 2])

    return im_color, im_falsecolor_r, im_falsecolor_g, im_falsecolor_b


if __name__  == '__main__' :
    im = cv.imread(
        "I:/LIP-dataset/TrainVal_parsing_annotations/TrainVal_parsing_annotations/train_segmentations/459_1209199.png")
    #im = cv.cvtColor(im, cv.COLOR_GRAY2BGR)
    im_color, im_falsecolor_r, im_falsecolor_g, im_falsecolor_b = applyCustomColorMap(im)

    cv.imshow("Colored Image", im_falsecolor_b)
    cv.waitKey(0)
    cv.destroyAllWindows()