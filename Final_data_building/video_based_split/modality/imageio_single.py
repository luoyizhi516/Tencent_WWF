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
    base='D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2-p3-merged/xuebao/videos/'
    save_dir='D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2-p3-merged/video_stat.csv'

    for i in os.listdir(base):
        vid_name=base+i
         
        vid = imageio.get_reader(vid_name,  'ffmpeg')
        #vid[0:1]
        for im in vid:
            data = skimage.img_as_float(im)
            data = data / data.max() #normalizes data in range 0 - 255
            data = 255 * data
            frame = data.astype(np.uint8)
            b, g, r = cv2.split(frame)
            modality='rgb'
            if np.mean(b-g)<5:
                modality="gray"
            frame=cv2ImgAddText(frame, modality , 50,50,(0,255,255),20)
            cv2.imshow('image', frame)  
            k = cv2.waitKey(30)  
            #q键退出
            if k==27:  
                break  
        
        cv2.destroyAllWindows()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()