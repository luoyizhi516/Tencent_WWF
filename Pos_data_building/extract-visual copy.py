# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import json

from xml.etree import ElementTree
from PIL import Image, ImageDraw, ImageFont
from collections import Counter

def path_replacement(file_path,dataset_name):
    if dataset_name in ['top14-part2','top14-part1']:
        file_path=file_path.replace('/Raw_Data/','/Raw_Data/top14-p1-p2/',1)
        #file_path=file_path.replace('D:/top14-dataset-part1','D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2')
    else:
        file_path=file_path.replace('-part','-p',1)
        file_path=file_path.replace('-raw/','/',1)
        file_path=file_path.replace('primary_supplement','sup9-p1')
    return file_path


def count_box(dataset_name,data_set='D:/WWF_Det/WWF_Data/Raw_Data/'):
    csv_file='D:/WWF_Det/WWF_Det/Raw_annoations/'+dataset_name+'.csv'
    df=pd.read_csv(csv_file)

    cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']
    box_num=0
    for index, row in tqdm(df.iterrows(), desc='Extracting data'):
        timu_data=json.loads(row['题目数据'])
        pic_id=row['题目ID']
        file_path=data_set+timu_data['Path']
        image_folder='D:/WWF_Det/WWF_Data/Pos_Data/'+dataset_name+'/allset/images/'
        text_folder='D:/WWF_Det/WWF_Data/Pos_Data/'+dataset_name+'/allset/labels/'
        if not os.path.exists(image_folder): 
            os.makedirs(image_folder, exist_ok = True)
        if not os.path.exists(text_folder): 
            os.makedirs(text_folder, exist_ok = True)
        file_path=path_replacement(file_path,dataset_name)

        assert os.path.exists(file_path),file_path

        index_pos=0 if dataset_name in ['top14-part2','top14-part1'] else 1
        cate=timu_data['Path'].split('/')[index_pos]
        image_name=str(pic_id)+'.jpg'
        label_dict=json.loads(row['标注答案'])
        #shutil.copyfile(file_path,image_folder+image_name)
        
        if len(label_dict.keys()):
            bboxes=label_dict['objects']
            box_num+=len(bboxes)
    return box_num

if __name__ == "__main__":
    all_box=0
    dataset_list=['sup9-part1','top14-part1','top14-part2','top14-part3',\
                'top14-part4','top14-part5','top14-part6','xuebao-120-all','top14-part7','top14-part8']
    for dataset in dataset_list:
        all_box+=count_box(dataset_name=dataset)
    print("Bounding box number:", all_box)