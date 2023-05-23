
# # Importing libraries 
# print('Importing libraries...')
# import os
# import cv2
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
# from deskew import determine_skew
# from typing import Tuple, Union
# from colorthief import ColorThief
# from google.colab.patches import cv2_imshow
# import math
# from skimage import io
# from skimage.color import rgb2gray
# import neurokit2 as nk
# from paddleocr import PaddleOCR
# print('Done.')

# # Importing models
# print('Importing models...') # FIX THIS TOO!!!
# ocr = PaddleOCR(use_angle_cls=True, lang='en', enable_mkldnn=True)
# !git clone https://github.com/ramsundar-tanikella/eff_net # FIX THIS!!!!
# segmentationModel = tf.keras.models.load_model('/content/eff_net/efficientnetB4_2.h5')
# segmentationModel.predict(np.zeros((1,380,380,3))) # To run it once so that weights get loaded into memory
# print('done')

from utilities import *

welcomeMessage()

def main():
    while True:
        print('> ', end='')
        try:
            a = input()
        except KeyboardInterrupt:
            break
        
        if a == '--help':
            helpFunction()
        
        if a == '--quit':
            break

        if a == '':
            continue

        a = a.split()

        if len(a) == 1:
            imageProcess(a)

        elif len(a) == 2:
            path = a[0]
            argument = a[1]

            if argument == '':
                imageProcess(path)
            elif argument == '-cp':
                imageProcess(path)
                croppedImageProcess(path)
            elif argument == '-v':
                videoProcess(path)
            elif argument == '-cv':
                videoProcess(path)
                croppedvideoProcess(path)
            else:
                argumentErrorPrompt()
                
        else:
            argumentErrorPrompt()

if __name__ == '__main__':
    main()
