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
    base='D:/WWF_Det\WWF_Data\Raw_Data/top14-p1-p2-p3-merged\baichunlu/videos/'
    for i in base:
        vid=base+i
        cap=cv2.VideoCapture(vid)
        while (cap.isOpened()):
            ret, frame = cap.read()
            if(frame.shape[2]==1):

                modality ='Gray'
            if(frame.shape[2] == 3):
                modality ='RGB'
                
            frame=cv2ImgAddText(frame, modality , 50,50,(0,255,255),20)
            cv2.imshow(frame)
            k=cv2.waitKey(0)
            if k & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
                        #img=cv2ImgAddText(img,str(pic_id),10,10,(0,0,0),30)
       
    #return df_store
if __name__ == "__main__":
    main()