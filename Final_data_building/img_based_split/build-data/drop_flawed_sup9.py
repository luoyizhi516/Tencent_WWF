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
    image_base,label_base='D:/WWF_Det/WWF_Data/Pos_Data/sup9-part1/valuableset-v/images/','D:/WWF_Det/WWF_Data/Pos_Data/sup9-part1/valuableset-v/labels/'
    x,y=os.listdir(image_base),os.listdir(label_base)
    #open('D:\WWF\data-check-list\check-list-part2\check-all-part2.txt','r')
    drop_list_x=np.unique(np.array([line2.replace('\n','',1)+'.jpg' for line2 in open(r'D:\WWF_Det\WWF_Det\Drop_txt\sup9-p1-all.txt')])).tolist()
    drop_list_y=np.unique(np.array([line2.replace('\n','',1)+'.txt' for line2 in open(r'D:\WWF_Det\WWF_Det\Drop_txt\sup9-p1-all.txt')])).tolist()
    print("Allset image number "+str(len(x)))
    print("Defected label number! "+str(len(drop_list_x)))
    
    # for i in drop_list_x:
    #      check_path=image_base+i
    #      assert os.path.exists(check_path),check_path+'not exists'
    droped_x=[i for i in x if i not in drop_list_x]
    
    droped_y=[i for i in y if i not in drop_list_y]
    print("Actual droped number during data spliting! "+str(len(x)-len(droped_x)))
    x_train,x_tar,y_train,y_tar=train_test_split(droped_x,droped_y,test_size=0.2,random_state=2021)
    train_folder_img,train_folder_txt='D:/WWF_Det/WWF_Data/Pos_Data/sup9-part1/conservation-v/train/images/','D:/WWF_Det/WWF_Data/Pos_Data/sup9-part1/conservation-v/train/labels/'
    test_folder_img,test_folder_txt='D:/WWF_Det/WWF_Data/Pos_Data/sup9-part1/conservation-v/val/images/','D:/WWF_Det/WWF_Data/Pos_Data/sup9-part1/conservation-v/val/labels/'
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
if __name__ == "__main__":
    
    main()