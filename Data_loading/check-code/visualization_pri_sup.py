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
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    # 判断是否为opencv图片类型
    if (isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype('simsun.ttc', textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)



def main():
    csv_file='D:/WWF\primary_sup_csv\data.csv'
    df=pd.read_csv(csv_file)
    data_set='D:/'
    box_num=0
    cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']
    for index, row in tqdm(df.iterrows()):
        timu_data=json.loads(row['题目数据'])
        pic_id=row['题目ID']
        file_path=data_set+timu_data['Path']
        
        visual_folder='D:/WWF/data/pri-sup-transformed/visualization/'

        if not os.path.exists(visual_folder): 
            os.makedirs(visual_folder, exist_ok = True)
        
        assert os.path.exists(file_path),file_path
        
        cate=timu_data['Path'].split('/')[1]
        image_name=str(pic_id)+'.jpg'
        label_dict=json.loads(row['标注答案'])
        if len(label_dict.keys()):
            bboxes=label_dict['objects']
            img = cv2.imread(file_path)
            imgy,imgx=img.shape[:2]
            #shutil.copyfile(file_path,visual_folder+image_name)
            
            if len(bboxes):
                for bbox in bboxes:
                    box_num+=1
                    topleft=np.array([int(max(bbox['data'][0]['x'],0)),int(max(bbox['data'][0]['y'],0))])
                    bottomrt=np.array([int(min(bbox['data'][2]['x'],imgx)),int(min(bbox['data'][2]['y'],imgy))])
                    center_x=int((topleft[0]+bottomrt[0])/2)
                    center_y=int((topleft[1]+bottomrt[1])/2)
                    cv2.rectangle(img, tuple(topleft), tuple(bottomrt),(0,255,0), 2, 4)
                    if len(bbox['tags']):
                        if 'value'in bbox['tags'][0].keys():
                            value=bbox['tags'][0]['value']+[cate]
                            class_name=str(value)
                            

                            img=cv2ImgAddText(img, class_name , center_x,center_y,(0,255,255),20)
                        #img=cv2ImgAddText(img,str(pic_id),10,10,(0,0,0),30)
        if not os.path.exists(visual_folder+image_name):
            cv2.imwrite(visual_folder+image_name,img)

    #return df_store
if __name__ == "__main__":
    main()