# -*- coding: UTF-8 -*-
from math import e
import os
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
    rawset_stat_path=r'D:\WWF_Det\WWF_Det\Raw_data_stat\top14-p1-p2-p3-merged\top14-p123-combine.csv'
    path_to_store='D:/WWF_Det/WWF_Det/Raw_data_stat/top14-p1-p2-p3-merged/split_condition.csv'
    df=pd.read_csv(rawset_stat_path)
    valued_df=df[~df.isnull().T.any()].drop(['video_path'], axis=1)
    cate_list=np.unique(valued_df['cate'].values)
    data_dict={'cate':cate_list,'infra_num':[],'rgb_num':[]}
    for cate in cate_list:
        data_dict['rgb_num'].append(valued_df.loc[(valued_df['cate'] == cate)&(valued_df['modality'] == 'RGB')].shape[0])
        data_dict['infra_num'].append(valued_df.loc[(valued_df['cate'] == cate)&(valued_df['modality'] == 'Infra')].shape[0])

    new_df=pd.DataFrame(data_dict)
    
    print(new_df)
if __name__ == "__main__":
    
    main()