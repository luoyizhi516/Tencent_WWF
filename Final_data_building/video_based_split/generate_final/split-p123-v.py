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
    pos_data_base='D:/WWF_Det/WWF_Data/Pos_Data/'
    raw_data_base='D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2-p3-merged/'
    annotation_base='D:/WWF_Det/WWF_Det/Raw_annoations/'
    vid_split_path='D:/WWF_Det/WWF_Det/Final_data_stat/top14-p123/video_split.csv'
    split_file='D:/WWF_Det/WWF_Det/Final_data_stat/top14-p123/img_split-v.csv'
    Final_data_base='D:/WWF_Det/WWF_Data/Final_Data/top14-p123-v/'
    train_img_dir,train_txt_dir=Final_data_base+'/train/images/',Final_data_base+'/train/labels/'
    test_img_dir,test_txt_dir=Final_data_base+'/val/images/',Final_data_base+'/val/labels/'
    if not os.path.exists(train_img_dir):os.makedirs(train_img_dir)
    if not os.path.exists(train_txt_dir):os.makedirs(train_txt_dir)
    if not os.path.exists(test_img_dir):os.makedirs(test_img_dir)
    if not os.path.exists(test_txt_dir):os.makedirs(test_txt_dir)
    data_dict={
        'img_path':[],
        'video_path':[],
        'cate':[],
        'modality':[],
        'label':[]
    }
    combine_data_list=['top14-part1','top14-part2','top14-part3']
    df_vid=pd.read_csv(vid_split_path)
    for dataset in combine_data_list:
        valuableset_dir=pos_data_base+dataset+'/valuableset-v/images/'
        valuableset_txt_dir=pos_data_base+dataset+'/valuableset-v/labels/'
        annotation_dir=annotation_base+dataset+'.csv'
        df=pd.read_csv(annotation_dir)
        pic_id_list=[i.replace('.jpg','',1) for i in os.listdir(valuableset_dir)]
        
        for pic_id in tqdm(pic_id_list):

            pic_df=df.loc[df['题目ID']== int(pic_id)]
            timu_str=pic_df['题目数据'].values[0]
            timu_data=json.loads(timu_str)
            video_path_list=timu_data['video_path'].split('/')
            vid_path=video_path_list[-3]+'/'+video_path_list[-2]+'/'+video_path_list[-1]
            pic_path=str(valuableset_dir+pic_id+'.jpg').replace('D:/WWF_Det/WWF_Data/Pos_Data/','')
            vid_df=df_vid.loc[df_vid['video_path']==raw_data_base+vid_path]
            label=vid_df['label'].values[0]
            modality=vid_df['modality'].values[0]
            cate=vid_df['cate'].values[0]
            if label=='train':
                shutil.copyfile(valuableset_dir+pic_id+'.jpg',train_img_dir+pic_id+'.jpg')
                shutil.copyfile(valuableset_txt_dir+pic_id+'.txt',train_txt_dir+pic_id+'.txt')
            elif label=='test':
                shutil.copyfile(valuableset_dir+pic_id+'.jpg',test_img_dir+pic_id+'.jpg')
                shutil.copyfile(valuableset_txt_dir+pic_id+'.txt',test_txt_dir+pic_id+'.txt')
            data_dict['img_path'].append(pic_path)
            data_dict['video_path'].append(vid_path)
            data_dict['cate'].append(cate)
            data_dict['modality'].append(modality)
            data_dict['label'].append(label)
            
    df_store=pd.DataFrame(data_dict)
    df_store.to_csv(split_file,index=False)
    print(df_store)
        #print(df_vid)
        #break

            

if __name__ == "__main__":
    
    main()