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



def main():
    dataset_name='top14-all/'
    base='D:/WWF_Det/WWF_Data/Raw_Data/'+dataset_name
    data_dict={
        'video_path':[],
        'cate':[],
        'modality':[]
    }
    save_base='D:/WWF_Det/WWF_Det/Raw_data_stat/'+dataset_name
    if not os.path.exists(save_base):os.makedirs(save_base)
    
    npy_path=save_base+'top14-all-modality.npy'
    df_path=save_base+'top14-all-modality.csv'
    
    for cate in tqdm(os.listdir(base)):
        cate_base=base+cate+'/videos/'
        modality_base=base+cate+'/modality/'
        if not os.path.exists(modality_base): os.makedirs(modality_base)
        for vid_name in tqdm(os.listdir(cate_base)):
            vid=cate_base+vid_name
            cap=cv2.VideoCapture(vid)
            ret, frame = cap.read()
            if not ret:
                modality=None 
                print(vid)
            elif ret:
                b, g, r = cv2.split(frame)
                if np.mean(b-g)<5:
                    modality="Infra"
                else: modality="RGB"
            
            data_dict['video_path'].append(vid)
            data_dict['cate'].append(cate)
            data_dict['modality'].append(modality)

            cap.release()
    np.save(npy_path,data_dict)
    df_store=pd.DataFrame(data_dict)
    df_store.to_csv(df_path,index=False)
if __name__ == "__main__":
    main()