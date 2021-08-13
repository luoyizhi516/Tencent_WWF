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
from collections import Counter
pos_data_base='D:/WWF_Det/WWF_Data/Pos_Data/'
raw_data_base='D:/WWF_Det/WWF_Data/Raw_Data/'

annotation_base='D:/WWF_Det/WWF_Det/Raw_annoations/'
cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']



combine_data_list=['rest-part1','rest-part2']
def cate_replacement(cate_name):
        ori_class=['laoshu','gaoyuanxuetu','chihu+shidiao','hongcuiya','paolu','huangyou']
        rename_class=['shu','gaoyuantu','chihu','hongzuishanya','pao','xiangyou']
        if cate_name in ori_class:
            for a,b in zip(ori_class,rename_class):
                if cate_name ==a:
                    cate_name=b
        return cate_name

source_vid_path_all=[]
for dataset in combine_data_list:
    source_vid_path_all=[]
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
        source_vid_path_all.append(source_base+vid_path)
            
source_vid_path_all=np.unique(np.array(source_vid_path_all)).tolist()
cate_list=dict(Counter([cate_replacement(i.split('/')[-3]) for i in source_vid_path_all]))
new_dict={'cate':[],'video_num':[],'split_condition':[]}
for i in cate_list:
    new_dict['cate'].append(i)
    new_dict['video_num'].append(cate_list[i])

    if i in cate_class:
        split_cond='exist cate'
    elif i not in cate_class:
        if cate_list[i]>=15:
            split_cond='video'
        else:
            split_cond='image'
    new_dict['split_condition'].append(split_cond)
    
df=pd.DataFrame(new_dict)
df=df.sort_values(by="video_num" , ascending=False)
df=df.reset_index().drop(['index'], axis=1)
#df.to_csv(r'D:\WWF_Det\WWF_Det\Final_data_stat\rest-cate\vid_stat.csv',index=False)

print(df)