# -*- coding: UTF-8 -*-
from math import e
import os
from numpy.lib.type_check import _imag_dispatcher
import pandas as pd
import shutil
import numpy as np
import cv2,glob
import random
from tqdm import tqdm
import pyfastcopy
import json,sklearn
from sklearn.model_selection import train_test_split
from collections import Counter

pos_data_base='D:/WWF_Det/WWF_Data/Pos_Data/'
raw_data_base='D:/WWF_Det/WWF_Data/Raw_Data/'

annotation_base='D:/WWF_Det/WWF_Det/Raw_annoations/'
cate_class=['baichunlu','chihu','gaoyuanshanchun','1gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']



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

    valuableset_dir=pos_data_base+dataset+'/allset/visualizations/'
    source_base=raw_data_base+dataset+'/'
    source_base=source_base.replace('part','p')
    annotation_dir=annotation_base+dataset+'.csv'
    df=pd.read_csv(annotation_dir)
    pic_id_list=[i.replace('.jpg','',1) for i in os.listdir(valuableset_dir)]
    for pic_id in (pic_id_list):

        pic_df=df.loc[df['题目ID']== int(pic_id)]
        timu_str=pic_df['题目数据'].values[0]
        timu_data=json.loads(timu_str)
        video_path_list=timu_data['video_path'].split('/')
        vid_path=video_path_list[-3]+'/'+video_path_list[-2]+'/'+video_path_list[-1]
        source_vid_path_all.append(source_base+vid_path)
            
source_vid_path_all=np.unique(np.array(source_vid_path_all)).tolist()

cate_list=dict(Counter([cate_replacement(i.split('/')[-3]) for i in source_vid_path_all]))
new_dict={'cate':[],'video_num':[],'split_condition':[]}
video_cate,image_cate,exist_cate=[],[],[]
for i in cate_list:
    new_dict['cate'].append(i)
    new_dict['video_num'].append(cate_list[i])

    if i in cate_class:
        split_cond='exist cate'
        exist_cate.append(i)
    elif i not in cate_class:
        if cate_list[i]>=15:
            split_cond='video'
            video_cate.append(i)
        else:
            split_cond='image'
            image_cate.append(i)
    new_dict['split_condition'].append(split_cond)
    
df=pd.DataFrame(new_dict)
df=df.sort_values(by="video_num" , ascending=False)
df=df.reset_index().drop(['index'], axis=1)

vid_dict={'video_path':[],'cate':[]
    }
raw_data_list=['rest-p1','rest-p2']
for dataset in raw_data_list:
    data_cate_list= os.listdir(raw_data_base + dataset)
    for i in video_cate:
        if i in data_cate_list:
            vid_folder=raw_data_base+dataset+'/'+i+'/videos/'
            vid_name=glob.glob(vid_folder+'*')
            vid_dict['video_path']+=vid_name
            vid_dict['cate']+=[i]*len(vid_name)



#df.to_csv(r'D:\WWF_Det\WWF_Det\Final_data_stat\rest-cate\vid_stat.csv',index=False)

vid_df=pd.DataFrame(vid_dict)
np.random.seed(2021)
for cate in video_cate:
    index=vid_df.loc[vid_df['cate'] == cate].sample(frac=1).index.values.tolist()
    print(index)
    test_num=int(df.loc[df['cate']==cate]['video_num']*0.2)
    test_index_all=index[:test_num]
    train_index_all=[i for i in index if i not in test_index_all]
    for ID in test_index_all:
        vid_df.loc[ID,'label']='test'
    for ID in train_index_all:
        vid_df.loc[ID,'label']='train'
    
print(vid_df)