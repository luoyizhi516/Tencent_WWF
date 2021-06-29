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
    base='D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2-p3-merged/chihu/videos/'
    save_dir='D:/WWF_Det/WWF_Data/Raw_Data/top14-p1-p2-p3-merged/video_stat.csv'

    for i in os.listdir(base):
        vid=base+i
        
        cap = cv2.VideoCapture(vid)  

        while 1:  
            ret, frame = cap.read()
            if ret:
                b, g, r = cv2.split(frame)

                modality='rgb'
                b,g,r=b.reshape(-1),g.reshape(-1),r.reshape(-1)
                if np.mean(b-g)<5:
                    modality="gray"
                frame=cv2ImgAddText(frame, modality , 50,50,(0,255,255),20)
                cv2.imshow('image', frame)  
                k = cv2.waitKey(30)  
                #q键退出
                if (k & 0xff == ord('q')):  
                    break  
            else: break
        cap.release()  
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()