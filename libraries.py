from tqdm import tqdm
bar = tqdm(total=16)

import cv2
bar.update(1)
import pandas as pd
bar.update(1)
import numpy as np
bar.update(1)
from deskew import determine_skew
bar.update(1)
import math
bar.update(1)
import os
bar.update(1)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
bar.update(1)


segmentationModel = tf.keras.models.load_model('/media/cornflaek/P' + 
'ersonal Stuff/my stuff/my schools stuff/college stuff/Inter IIT ' + 
'tech 2022 shit/final/efficientnetB4_2.h5')
bar.update(1)

from paddleocr import PaddleOCR
bar.update(1)
from colorthief import ColorThief
bar.update(1)
from skimage.color import rgb2gray
bar.update(1)
from skimage import io
bar.update(1)
import neurokit2 as nk
bar.update(1)
import matplotlib.pyplot as plt
bar.update(1)

ocr = PaddleOCR(use_angle_cls=True, lang='en', enable_mkldnn=True, show_log=False)
bar.update(1)

bar.close()