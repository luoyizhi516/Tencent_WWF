# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import random
import json,sklearn
from sklearn.model_selection import train_test_split



def main():
    sample_range=[0,30]
    #This is the base for all raw dataset that is subjected to be labeled
    allset_base='D:/top14-dataset/'
    #This is the base for the subset that is already label and will be droped later
    subset_base='D:/top14-dataset-part1/'

    allset_cate_list=os.listdir(allset_base)
    #subset_cate_list=os.listdir(subset_base)

    for cate in tqdm(allset_cate_list):
        print('Processing '+cate)
        allset_cate_video_dir=allset_base+cate+'/videos/'
        subset_cate_video_dir=subset_base+cate+'/videos/'
        assert os.path.exists(subset_cate_video_dir),subset_cate_video_dir+' not exists!'
        allset_video=os.listdir(allset_cate_video_dir)
        subset_video=os.listdir(subset_cate_video_dir)
        
        random.seed(2021)
        droped_video=[i for i in allset_video if i not in subset_video]
        random.shuffle(droped_video)
        sample_video=droped_video[sample_range[0]:sample_range[1]]
        newset_base='D:/WWF/data/top14-part3-raw/'
        newset_cate_video_dir=newset_base+cate+'/videos/'
        if not os.path.exists(newset_cate_video_dir): os.makedirs(newset_cate_video_dir)
        for vid in sample_video:

            shutil.copyfile(allset_cate_video_dir+vid,newset_cate_video_dir+vid)
    print("Sampling is done!")
if __name__ == "__main__":
    
    main()