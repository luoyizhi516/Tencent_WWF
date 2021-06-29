# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import json
import imageio,skimage
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
    return modality
def main():
    dataset_name='top14-all/'
    save_base='D:/WWF_Det/WWF_Det/Raw_data_stat/'+dataset_name
    df_path=save_base+'top14-all-modality.csv'
    df_pos=save_base+'top14-all-pos.csv'
    df=pd.read_csv(df_path)
    null_df=df[df.isnull().T.any()]
    for index, row in null_df.iterrows():
        video_path=row['video_path']
        try:
            modality=imageio_stat(video_path)
        except:
            print(video_path)
            continue
        else:
            df.loc[index,'modality']=modality

    print(df[df.isnull().T.any()])
    df.to_csv(df_pos,index=False)
if __name__ == "__main__":
    main()