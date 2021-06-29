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
    if (isinstance(img, np.ndarray)):
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype('simsun.ttc', textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

def main():
    base='D:/WWF_Det/WWF_Data/Raw_Data/top14-all/'
    for cate in tqdm(os.listdir(base)[1:4]):
        cate_base=base+cate+'/videos/'
        modality_base=base+cate+'/modality/'
        if not os.path.exists(modality_base): os.makedirs(modality_base)
        for vid_name in tqdm(os.listdir(cate_base)):
            vid=cate_base+vid_name
            cap=cv2.VideoCapture(vid)
            ret, frame = cap.read()
            if not ret: print(vid)
            if ret:
                b, g, r = cv2.split(frame)
                b,g,r=b.reshape(-1),g.reshape(-1),r.reshape(-1)
                if np.mean(b-g)<5:
                    modality="Infra"
                else: modality="RGB"
                frame=cv2ImgAddText(frame, modality , 100,100,(255,0,0),50)
                #print(modality_base+vid_name[:-4])
                cv2.imwrite(modality_base+vid_name[:-4]+'.jpg',frame)
            cap.release()
if __name__ == "__main__":
    main()