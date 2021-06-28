# -*- coding: UTF-8 -*-
from math import e
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
    rawset_name='top14-p1-p2/'
    rawdata_base='D:/WWF_Det/WWF_Data/Raw_Data/'
    cate_dir=rawdata_base+rawset_name
    cate_list=os.listdir(cate_dir)
    random.seed(2021)
    for cate in cate_list:
        videoset_dir=cate_dir+cate+'/videos/'
        video_id=os.listdir(videoset_dir)
        random.shuffle(video_id)
        train_id=video_id[:-20]
        test_id=video_id[-20:]
        
        print(train_id)
        print(test_id)
        break
if __name__ == "__main__":
    
    main()