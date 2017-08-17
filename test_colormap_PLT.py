#coding=utf8

from skimage import measure,color
import matplotlib.pyplot as plt
import cv2 as cv

data = cv.imread(
    "I:/LIP-dataset/TrainVal_parsing_annotations/TrainVal_parsing_annotations/train_segmentations/459_1209199.png",
    cv.IMREAD_GRAYSCALE)

labels=measure.label(data,connectivity=2)               #8连通区域标记
print labels
dst=color.label2rgb(labels)                             #根据不同的标记显示不同的颜色
print('regions number:',labels.max()+1)                 #显示连通区域块数(从0开始标记)

fig, (ax1) = plt.subplots(1)
ax1.imshow(dst,interpolation='nearest')
plt.show()