# -*- coding: UTF-8 -*-
from math import e
import os
from typing import final
from numpy.lib.type_check import _imag_dispatcher
import pandas as pd
import shutil
import numpy as np
import cv2
import random
from tqdm import tqdm
import pyfastcopy
import json,sklearn
from sklearn.model_selection import train_test_split



def main():
    increment_datasets=['top14-part4','top14-part5','top14-part6','top14-part7','top14-part8','xuebao-120-all']
    suplement_datasets=['sup9-part1']
    splited_data_base='D:/WWF_Det/WWF_Data/Final_Data/top14-p123/'
    final_data_base='D:/WWF_Det/WWF_Data/Final_Data/top23-p12345678-p1-xuebao/'
    os.system("cp -R "+splited_data_base+' '+final_data_base)
    for i in increment_datasets:
        valuableset='D:/WWF_Det/WWF_Data/Pos_Data/'+i+'/valuableset/'
        train_set=os.path.join(final_data_base,'train')
        os.system("cp -r "+valuableset+'* '+train_set)
    for i in suplement_datasets:
        valuableset_train='D:/WWF_Det/WWF_Data/Pos_Data/'+i+'/conservation/train/'
        valuableset_val='D:/WWF_Det/WWF_Data/Pos_Data/'+i+'/conservation/val/'
        train_set=os.path.join(final_data_base,'')
        val_set=os.path.join(final_data_base,'')
        os.system("cp -r "+valuableset_train+' '+train_set)
        os.system("cp -r "+valuableset_val+' '+val_set)
if __name__ == "__main__":
    
    main()