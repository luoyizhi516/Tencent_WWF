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
    csv_file='D:/WWF_Det/WWF_Det/Raw_annoations/xuebao-120-all.csv'
    df=pd.read_csv(csv_file)
    data_set='D:/WWF_Det/WWF_Data/Raw_Data/'
    box_num=0
    cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']
    #cate_class=['person','chihu','zanghu','yang','maoniu','lanmaji','xuebao','gaoyuantu','yanyang']
    for index, row in tqdm(df.iterrows()):
        timu_data=json.loads(row['题目数据'])
        pic_id=row['题目ID']
        file_path=data_set+timu_data['Path']
        image_folder='D:/WWF_Det/WWF_Data/Pos_Data/xuebao-120-all/allset/images/'
        text_folder='D:/WWF_Det/WWF_Data/Pos_Data/xuebao-120-all/allset/labels/'
        if not os.path.exists(image_folder): 
            os.makedirs(image_folder, exist_ok = True)
        if not os.path.exists(text_folder): 
            os.makedirs(text_folder, exist_ok = True)
        assert os.path.exists(file_path),file_path
        
        cate=timu_data['Path'].split('/')[1]
        image_name=str(pic_id)+'.jpg'
        label_dict=json.loads(row['标注答案'])
        shutil.copyfile(file_path,image_folder+image_name)
        if len(label_dict.keys()):
            bboxes=label_dict['objects']
            img = cv2.imread(file_path)
            imgy,imgx=img.shape[:2]
            txt_path=text_folder+os.path.splitext(image_name)[0]+'.txt'
            
            with open(txt_path, 'w') as f:
                for bbox in bboxes:
                    x_list=[bbox['data'][i]['x'] for i in range(0,4)]
                    y_list=[bbox['data'][i]['y'] for i in range(0,4)]
                    topleft=[max(min(x_list),0),max(min(y_list),0)]
                    bottomright=[min(max(x_list),imgx-1),min(max(y_list),imgy-1)]
                    center_x=((topleft[0]+bottomright[0])/2)/imgx
                    center_y=((topleft[1]+bottomright[1])/2)/imgy
                    w=abs(bottomright[0]-topleft[0])/imgx
                    h=abs(bottomright[1]-topleft[1])/imgy
                    
                    cate_id=cate_class.index(cate)
    
                    f.write(str(cate_id)+' '+str(center_x)+' '+str(center_y)+' '+str(w)+' '+str(h)+'\n')
   
    
     
    #return df_store
if __name__ == "__main__":
    
    main()