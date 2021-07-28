# -*- coding: UTF-8 -*-
from math import e, inf
import os
from numpy.lib.type_check import _imag_dispatcher
import pandas as pd
import shutil
import numpy as np
import cv2
import random
from tqdm import tqdm
import pyfastcopy
import json,sklearn
from sklearn.model_selection import train_test_split
from datetime import datetime

def vtf(path):
     videoCapture = cv2.VideoCapture()
     videoCapture.open(path)
     fps = videoCapture.get(cv2.CAP_PROP_FPS) 
     frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
     print("fps=", int(fps), "frames=", int(frames))
     for i in range(int(frames)):
          ret, frame = videoCapture.read()

          cv2.imwrite("D:\WWF_Det\WWF_Data\Final_Data\gaoyuantu-frame/%d.jpg"%(i), frame)

    

if __name__ == "__main__":
    
    t1 = datetime.now()
    vtf("D:/WWF_Det/WWF_Data/Final_Data/valset-vid-v1/gaoyuantu/00143.AVI")
    t2 = datetime.now()
    print("Time cost = ", (t2 - t1))