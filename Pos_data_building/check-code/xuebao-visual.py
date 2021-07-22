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
    csv_file='D:/WWF_Det/WWF_Det/Raw_annoations/xuebao-120-all.csv'
    df=pd.read_csv(csv_file)
    data_set='D:/WWF_Det/WWF_Data/Raw_Data/'
    box_num=0
    cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu','chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']
    txt_path=r'D:\WWF_Det\WWF_Det\Drop_txt\xuebao-120-all/extra.txt'
    position_list=['目标类别物体出现比例-全部出现','目标类别物体出现比例-部分出现','未知类别全部出现','未知类别部分出现']
    with open(txt_path, 'w') as f:
        for index, row in tqdm(df.iterrows()):
            timu_data=json.loads(row['题目数据'])
            pic_id=row['题目ID']
            file_path=data_set+timu_data['Path']
            
            visual_folder='D:/WWF_Det/WWF_Data/Pos_Data/xuebao-120-all-improved/allset/visualizations/'

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
                
                if len(bboxes):
                    for bbox in bboxes:
                        box_num+=1
                        x_list=[bbox['data'][i]['x'] for i in range(0,4)]
                        y_list=[bbox['data'][i]['y'] for i in range(0,4)]
                        topleft=[int(max(min(x_list),0)),int(max(min(y_list),0))]
                        bottomright=[int(min(max(x_list),imgx-1)),int(min(max(y_list),imgy-1))]
                        cv2.rectangle(img, tuple(topleft), tuple(bottomright),(0,255,0), 2, 4)
                        center_x=int((topleft[0]+bottomright[0])/2)
                        center_y=int((topleft[1]+bottomright[1])/2)
                        if len(bbox['tags']):
                            if 'value'in bbox['tags'][0].keys():
                                value=bbox['tags'][0]['value']+[cate]
                                class_name=str(value)

                                img=cv2ImgAddText(img, class_name , int(topleft[0]),center_y,(0,255,255),20)
                                inter=len(set(value)&set(position_list))
                                if inter==0:
                                    f.write(str(pic_id)+'\n')
                            else:
                                print('error')
                                f.write(str(pic_id)+'\n')

                        else:
                            print(pic_id,'value missing')
                            f.write(str(pic_id)+'\n')

                elif not len(bboxes):
                    print('no box')
                    f.write(str(pic_id)+'\n')
                #ONLY plot the image if it is labeled.
                if not os.path.exists(visual_folder+image_name):
                    cv2.imwrite(visual_folder+image_name,img)


    #return df_store
if __name__ == "__main__":
    main()