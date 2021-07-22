# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import json,sklearn
from sklearn.model_selection import train_test_split



def main():
    image_base,label_base='D:/WWF_Det\WWF_Data\Pos_Data\sup9-part1/allset/images/','D:/WWF_Det\WWF_Data\Pos_Data\sup9-part1/allset/labels/'
    x,y=os.listdir(image_base),os.listdir(label_base)
    x_train,x_tar,y_train,y_tar=train_test_split(_,y,test_size=0.2,random_state=2021)
    train_folder_img,train_folder_txt='D:/WWF_Det\WWF_Data\Pos_Data\sup9-part1/conservation/train/images/','D:/WWF_Det\WWF_Data\Pos_Data\sup9-part1/conservation/train/labels/'
    test_folder_img,test_folder_txt='D:/WWF_Det\WWF_Data\Pos_Data\sup9-part1/conservation/val/images/','D:/WWF_Det\WWF_Data\Pos_Data\sup9-part1/conservation/val/labels/'
    if not os.path.exists(train_folder_img): os.makedirs(train_folder_img)
    if not os.path.exists(train_folder_txt): os.makedirs(train_folder_txt)
    if not os.path.exists(test_folder_img): os.makedirs(test_folder_img)
    if not os.path.exists(test_folder_txt): os.makedirs(test_folder_txt)
    for x_t, y_t in tqdm(zip(x_train,y_train)):
        shutil.copyfile(image_base+x_t,train_folder_img+x_t)
        shutil.copyfile(label_base+y_t,train_folder_txt+y_t)
    for x_t, y_t in tqdm(zip(x_tar,y_tar)):
        shutil.copyfile(image_base+x_t,test_folder_img+x_t)
        shutil.copyfile(label_base+y_t,test_folder_txt+y_t)
    #print(x_train)
if __name__ == "__main__":
    
    main()