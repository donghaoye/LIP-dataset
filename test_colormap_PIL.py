from PIL import Image
import numpy as np

im = Image.open("I:/LIP-dataset/TrainVal_parsing_annotations/TrainVal_parsing_annotations/train_segmentations/459_1209199.png")
palette=[]
# for i in range(256):
#     palette.extend((i,i,i))
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
print palette
im.putpalette(palette)
im.show()