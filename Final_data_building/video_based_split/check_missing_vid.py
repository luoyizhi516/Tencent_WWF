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



def main():
    frame_base=r"D:\WWF_Det\WWF_Data\Final_Data\valset-frames-v1/"
    video_base=r"D:\WWF_Det\WWF_Data\Final_Data\valset-vid-v1/"
    missing_vid={}
    for cate in os.listdir(video_base):
            
        frame_dir=frame_base+cate+'/'
        video_dir=video_base+cate+'/'
        frame_vid_name=np.unique(np.array([i.split('-')[0] for i in os.listdir(frame_dir)])).tolist()
        missing_vid[cate]=[i.split('.')[0] for i in os.listdir(video_dir) if i.split('.')[0] not in frame_vid_name]
    print(missing_vid)

if __name__ == "__main__":
    
    main()