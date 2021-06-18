# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import json




def main():
    csv_file='C:/Users\luxiferchen\Downloads\物体检测标注-j22eo7_20210615211440003.csv'
    df=pd.read_csv(csv_file)
    data_set='D:/top14-dataset-part1/'
    box_num=0
    cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']
    #cate_class=['person','chihu','zanghu','yang','maoniu','lanmaji','xuebao','gaoyuantu','yanyang']
    for index, row in tqdm(df.iterrows()):
        timu_data=json.loads(row['题目数据'])
        pic_id=row['题目ID']
        file_path=data_set+timu_data['Path']
        image_folder='data/top14-sup-transformed/allset/images/'
        text_folder='data/top14-sup-transformed/allset/labels/'
        if not os.path.exists(image_folder): 
            os.makedirs(image_folder, exist_ok = True)
        if not os.path.exists(text_folder): 
            os.makedirs(text_folder, exist_ok = True)
        assert os.path.exists(file_path),file_path
        
        cate=timu_data['Path'].split('/')[0]
        #image_name=cate+timu_data['Path'].split('/')[2]
        image_name=str(pic_id)+'.jpg'
        label_dict=json.loads(row['标注答案'])
        if len(label_dict.keys()):
            bboxes=label_dict['objects']
            img = cv2.imread(file_path)
            imgy,imgx=img.shape[:2]
            shutil.copyfile(file_path,image_folder+image_name)
            txt_path=text_folder+os.path.splitext(image_name)[0]+'.txt'
            
            with open(txt_path, 'w') as f:
                for bbox in bboxes:
                    box_num+=1
                    topleft=[max(bbox['data'][0]['x'],0),max(bbox['data'][0]['y'],0)]
                    bottomright=[min(bbox['data'][2]['x'],imgx),min(bbox['data'][2]['y'],imgy)]
                    center_x=((topleft[0]+bottomright[0])/2)/imgx
                    center_y=((topleft[1]+bottomright[1])/2)/imgy
                    w=abs(bottomright[0]-topleft[0])/imgx
                    h=abs(bottomright[1]-topleft[1])/imgy
                    
                    cate_id=cate_class.index(cate)
    
                    f.write(str(cate_id)+' '+str(center_x)+' '+str(center_y)+' '+str(w)+' '+str(h)+'\n')
   
    
     
    #return df_store
if __name__ == "__main__":
    
    main()