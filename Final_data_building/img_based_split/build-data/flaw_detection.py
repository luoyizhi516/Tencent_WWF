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
    image_base,label_base='D:/WWF/data/top14-part1-transformed/allset/images/','D:/WWF/data/top14-part1-transformed/allset/labels/'
    x,y=os.listdir(image_base),os.listdir(label_base)
    drop_list_x=np.unique(np.array([line2.replace('\n','',1)+'.jpg' for line2 in open("D:\WWF\data-check-list\check_list\check-all.txt")])).tolist()
    drop_list_y=np.unique(np.array([line2.replace('\n','',1)+'.txt' for line2 in open("D:\WWF\data-check-list\check_list\check-all.txt")])).tolist()
    print("Allset image number "+str(len(x)))
    print("Defected label number! "+str(len(drop_list_x)))
    

    droped_x=[i for i in x if i not in drop_list_x]
    
    droped_y=[i for i in y if i not in drop_list_y]
    print("Actual droped number during data spliting! "+str(len(x)-len(droped_x)))
   
if __name__ == "__main__":
    
    main()