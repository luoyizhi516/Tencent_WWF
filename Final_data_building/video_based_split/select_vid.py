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

pos_data_base='D:/WWF_Det/WWF_Data/Pos_Data/'
raw_data_base='D:/WWF_Det/WWF_Data/Raw_Data/'

annotation_base='D:/WWF_Det/WWF_Det/Raw_annoations/'

Final_data_base='D:/WWF_Det/WWF_Data/Final_Data/rest-vid-clean/'
try:
    os.makedirs(Final_data_base)
except:
    pass

combine_data_list=['rest-part1','rest-part2']


for dataset in combine_data_list:
    source_vid_path_all=[]
    target_vid_path_all=[]
    valuableset_dir=pos_data_base+dataset+'/allset/visualizations/'
    source_base=raw_data_base+dataset+'/'
    source_base=source_base.replace('part','p')
    annotation_dir=annotation_base+dataset+'.csv'
    df=pd.read_csv(annotation_dir)
    pic_id_list=[i.replace('.jpg','',1) for i in os.listdir(valuableset_dir)]
    for pic_id in tqdm(pic_id_list):

            pic_df=df.loc[df['题目ID']== int(pic_id)]
            timu_str=pic_df['题目数据'].values[0]
            timu_data=json.loads(timu_str)
            video_path_list=timu_data['video_path'].split('/')
            vid_path=video_path_list[-3]+'/'+video_path_list[-2]+'/'+video_path_list[-1]
            source_vid_path_all.append(vid_path)
            target_vid_path_all.append(video_path_list[-3]+'-'+video_path_list[-1])
    source_vid_path_all=np.unique(np.array(source_vid_path_all)).tolist()
    target_vid_path_all=np.unique(np.array(target_vid_path_all)).tolist()

    for source_vid,target_vid in zip(source_vid_path_all,target_vid_path_all):
            shutil.copyfile(source_base+source_vid,Final_data_base+target_vid)   