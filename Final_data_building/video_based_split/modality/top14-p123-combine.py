# -*- coding: UTF-8 -*-
import os
from ssl import VERIFY_DEFAULT
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import json
import imageio
import skimage
from xml.etree import ElementTree
from PIL import Image, ImageDraw, ImageFont
def imageio_stat(video_path):
    vid = imageio.get_reader(video_path,  'ffmpeg')
    first=True
    for i in vid:
        im=i
        first=False
        if not first:
            break
    data = skimage.img_as_float(im)
    data = data / data.max() #normalizes data in range 0 - 255
    data = 255 * data
    frame = data.astype(np.uint8)
    b, g, r = cv2.split(frame)
    if np.mean(b-g)<5:
        modality="Infra"
    else: modality="RGB"
    return modality,frame

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype('simsun.ttc', textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def main():
    base='D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2-p3-merged/'
    dataset_name='top14-p1-p2-p3-merged/'
    save_base='D:/WWF_Det/WWF_Det/Raw_data_stat/'+dataset_name
    if not os.path.exists(save_base):os.makedirs(save_base)
    df_path=save_base+'top14-p123-combine.csv'
    data_dict={
        'video_path':[],
        'cate':[],
        'modality':[]
    }
    for cate in tqdm(os.listdir(base)):
        cate_base=base+cate+'/videos/'
        modality_base=base+cate+'/modality/'
        if not os.path.exists(modality_base): os.makedirs(modality_base)
        for vid_name in tqdm(os.listdir(cate_base)):
            vid_id=cate_base+vid_name
            cap=cv2.VideoCapture(vid_id)
            ret, frame = cap.read()
            data_dict['video_path'].append(vid_id)
            data_dict['cate'].append(cate)
            if not ret: 
                try:
                    modality_imageio,frame_imageio=imageio_stat(vid_id)
                except:
                    modality=None
                    data_dict['modality'].append(modality)
                    print(vid_id)
                    continue
                else:
                    modality,frame=modality_imageio,frame_imageio
                    
            if ret:
                b, g, r = cv2.split(frame)
                if np.mean(b-g)<5:
                    modality="Infra"
                else: modality="RGB"
        
            data_dict['modality'].append(modality)
            frame=cv2ImgAddText(frame, modality , 100,100,(255,0,0),50)

            cv2.imwrite(modality_base+vid_name[:-4]+'.jpg',frame)
    df=pd.DataFrame(data_dict)
    df.to_csv(df_path,index=False)
    df=pd.read_csv(df_path)
    print(df[df.isnull().T.any()])
if __name__ == "__main__":
    main()