# -*- coding: UTF-8 -*-
from math import e
import os
from numpy.lib.type_check import _imag_dispatcher
import pandas as pd
import shutil
import numpy as np
import cv2

from tqdm import tqdm
import pyfastcopy
import json,sklearn
from sklearn.model_selection import train_test_split

def combine_transform(base,save_dir):
    trans_file_list=os.listdir(base)
    create_new=True
    for trans in trans_file_list:
        df=pd.read_csv(base+trans)

        if create_new:
            df_all=df
            create_new=False
            continue
        df_all=pd.concat([df_all,df])
    df_all.to_csv(save_dir,index=False,encoding="utf_8_sig")
    return df_all

def main():
    
    annotation_base=r'D:\WWF_Det\WWF_Det\Raw_annoations\top14-part5/'
    save_dir=r'D:\WWF_Det\WWF_Det\Raw_annoations\top14-part5.csv'
    combine_transform(annotation_base,save_dir)
if __name__ == "__main__":
    
    main()