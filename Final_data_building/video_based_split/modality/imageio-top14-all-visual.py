# -*- coding: UTF-8 -*-
import os
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

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype('simsun.ttc', textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def main():
    base='D:/WWF_Det/WWF_Data/Raw_Data/top14-all/'
    
    for cate in tqdm(os.listdir(base)):
        cate_base=base+cate+'/videos/'
        modality_base=base+cate+'/modality/'
        if not os.path.exists(modality_base): os.makedirs(modality_base)
        for vid_name in tqdm(os.listdir(cate_base)):
            vid_id=cate_base+vid_name
            vid = imageio.get_reader(vid_id,  'ffmpeg')
            im=[i for i in vid]
            #im=[i for num,i in enumerate(vid) if num==0]
            data = skimage.img_as_float(im[0])
            data = data / data.max() #normalizes data in range 0 - 255
            data = 255 * data
            frame = data.astype(np.uint8)
            b, g, r = cv2.split(frame)
            if np.mean(b-g)<5:
                modality="Infra"
            else: modality="RGB"
            frame=cv2ImgAddText(frame, modality , 100,100,(255,0,0),50)

            cv2.imwrite(modality_base+vid_name[:-4]+'.jpg',frame)
if __name__ == "__main__":
    main()