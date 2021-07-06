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
    increment_datasets=['top14-part4']
    suplement_datasets=['sup9-part1']
    splited_data_base='D:/WWF_Det/WWF_Data/Final_Data/top14-p123/'
    final_data_base='D:/WWF_Det/WWF_Data/Final_Data/top23-p1234-p1/'
    os.system("cp -r "+splited_data_base+' '+final_data_base)
    for i in increment_datasets:
        valuableset='D:/WWF_Det/WWF_Data/Pos_Data/'+i+'/valuableset/'
        train_set=os.path.join(final_data_base,'train')
        os.system("cp -r "+valuableset+' '+train_set)
    for i in suplement_datasets:
        valuableset_train='D:/WWF_Det/WWF_Data/Pos_Data/'+i+'/conservation/train/'
        valuableset_val='D:/WWF_Det/WWF_Data/Pos_Data/'+i+'/conservation/val/'
        train_set=os.path.join(final_data_base,'')
        val_set=os.path.join(final_data_base,'')
        os.system("cp -r "+valuableset_train+' '+train_set)
        os.system("cp -r "+valuableset_val+' '+val_set)
if __name__ == "__main__":
    
    main()