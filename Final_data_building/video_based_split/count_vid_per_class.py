# -*- coding: UTF-8 -*-

import os
from collections import Counter
import pandas as pd
import shutil
import numpy as np

import random
from tqdm import tqdm
import pyfastcopy
import json,sklearn
from sklearn.model_selection import train_test_split
def cate_replacement(cate_name):
        ori_class=['laoshu','gaoyuanxuetu','chihu+shidiao','hongcuiya','paolu','huangyou']
        rename_class=['shu','gaoyuantu','chihu','hongzuishanya','pao','xiangyou']
        if cate_name in ori_class:
            for a,b in zip(ori_class,rename_class):
                if cate_name ==a:
                    cate_name=b
        return cate_name

Final_vid_base='D:/WWF_Det/WWF_Data/Final_Data/rest-vid-clean/'
vid_list=os.listdir(Final_vid_base)
cate_list=dict(Counter([cate_replacement(i.split('-')[0]) for i in vid_list]))
new_dict={'cate':[],'video_num':[]}
for i in cate_list:
    new_dict['cate'].append(i)
    new_dict['video_num'].append(cate_list[i])
df=pd.DataFrame(new_dict)
df=df.sort_values(by="video_num" , ascending=False)
df=df.reset_index().drop(['index'], axis=1)
df.to_csv(r'D:\WWF_Det\WWF_Det\Final_data_stat\rest-cate\vid_stat.csv',index=False)

print(df)