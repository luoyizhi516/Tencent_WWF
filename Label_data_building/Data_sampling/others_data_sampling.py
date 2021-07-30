# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import random
import json,sklearn
from glob import glob
from sklearn.model_selection import train_test_split



def main():
    cate_class=['baichunlu','chihu','gaoyuanshanchun','gaoyuantu','lanmaji','ma','malu','maoniu','mashe','person','xuebao','yang','yanyang','zanghu',\
        'chai','hanta','huangmomao','lang','lv','pao','sheli','shidiao','zongxiong']
    original_base='D:/other_cate/'
    new_base='D:/rest_cate/'
    undone_list=[cate for cate in os.listdir(original_base) if cate not in cate_class]
    for i in undone_list:
        os.system('cp - R '+original_base+i+' '+new_base+i+'/')
        
if __name__ == "__main__":
    
    main()