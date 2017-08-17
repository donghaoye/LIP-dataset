#coding=utf8

import os
import numpy as np
from PIL import Image


# 取得目录下面的文件列表
def get_dir_img_list(dir_proc, recusive=True):
    file_list = []
    for file in os.listdir(dir_proc):
        if os.path.isdir(os.path.join(dir_proc, file)):
            if (recusive):
                file_list.append(get_dir_img_list(os.path.join(dir_proc, file), recusive))
            continue
        #img = os.path.join(dir_proc, file)
        img = dir_proc + "/" + file
        file_list.append(img)
    return file_list


palette=[]
palette[:3*21]=np.array([[0, 0, 0],
                            [128, 0, 0],
                            [0, 128, 0],
                            [128, 128, 0],
                            [0, 0, 128],
                            [128, 0, 128],
                            [0, 128, 128],
                            [128, 128, 128],
                            [64, 0, 0],
                            [192, 0, 0],
                            [64, 128, 0],
                            [192, 128, 0],
                            [64, 0, 128],
                            [192, 0, 128],
                            [64, 128, 128],
                            [192, 128, 128],
                            [0, 64, 0],
                            [128, 64, 0],
                            [0, 192, 0],
                            [128, 192, 0],
                            [0, 64, 128]], dtype='uint8').flatten()

if __name__=="__main__":
    pasing_dir = "I:/LIP-dataset/TrainVal_parsing_annotations/TrainVal_parsing_annotations/train_segmentations"
    pasing_img_list = get_dir_img_list(pasing_dir)

    img_dir = "I:/LIP-dataset/TrainVal_images/TrainVal_images/train_images"
    img_list = get_dir_img_list(img_dir)

    for img_path in pasing_img_list:
        img = Image.open(img_path)
        img.putpalette(palette)
        img.show()
        #break

    for img_path in img_list:
        img = Image.open(img_path)
        img.show()
        #break



