# Importing libraries 
print('Importing libraries...')
import os
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from deskew import determine_skew
from typing import Tuple, Union
from colorthief import ColorThief
import math
from skimage import io
from skimage.color import rgb2gray
import neurokit2 as nk
from paddleocr import PaddleOCR
import sys
print('Done.\n')

# Importing models
print('\nImporting models...') # FIX THIS TOO!!!
ocr = PaddleOCR(use_angle_cls=True, lang='en', enable_mkldnn=True)

from utilities import *

welcomeMessage()

def main():
    while True:
        print('> ', end='')
        a = []
        try:
            a = processInput()
        except KeyboardInterrupt:
            break

        if len(a) == 1:
            path = a[0]
            if path.lower() == '--help':
                helpFunction()
        
            if path.lower() == '--quit':
                break

            if path == '':
                continue
            
            imageProcess(path, 'vitals.csv')

        elif len(a) == 2:
            path = a[0]
            argument = a[1]

            if argument == '':
                imageProcess(path, 'vitals.csv')
            elif argument == '-cp':
                imageProcess(path, 'vitals.csv')
                croppedImageProcess(path, 'output' + '-cropped.jpeg')
            elif argument == '-v':
                videoProcess(path, 'vitals.csv')
            elif argument == '-cv':
                videoProcess(path, 'vitals.csv')
                croppedvideoProcess(path, 'output' + '-cropped.jpeg')
            else:
                argumentErrorPrompt()

        elif len(a) == 3:
            path = a[0]
            argument = a[1]
            savepath = a[2]

            if argument == '':
                imageProcess(path, savepath + '\\vitals.csv')
            elif argument == '-cp':
                imageProcess(path, savepath + '\\vitals.csv')
                croppedImageProcess(path, savepath + '\\output' + '-cropped.jpeg')
            elif argument == '-v':
                videoProcess(path, savepath + '\\vitals.csv')
            elif argument == '-cv':
                videoProcess(path, savepath + '\\vitals.csv')
                croppedvideoProcess(path, savepath + '\\output' + '-cropped.jpeg')
            else:
                argumentErrorPrompt()
        else:
            argumentErrorPrompt()

if __name__ == '__main__':
    main()
