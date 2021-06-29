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
    rawset_stat_path='D:/WWF_Det/WWF_Det/Raw_data_stat/top14-all/top14-all-pos.csv'
    path_to_store='D:/WWF_Det/WWF_Det/Raw_data_stat/top14-all/split_critiria.csv'
    df=pd.read_csv(rawset_stat_path)
    valued_df=df[~df.isnull().T.any()].drop(['video_path'], axis=1)
    cate_list=np.unique(valued_df['cate'].values)
    data_dict={'cate':cate_list,'infra_num':[],'rgb_num':[]}
    for cate in cate_list:
        data_dict['rgb_num'].append(valued_df.loc[(valued_df['cate'] == cate)&(valued_df['modality'] == 'RGB')].shape[0])
        data_dict['infra_num'].append(valued_df.loc[(valued_df['cate'] == cate)&(valued_df['modality'] == 'Infra')].shape[0])
    data_dict['infra_test']=np.round((np.array(data_dict['infra_num'])/(np.array(data_dict['rgb_num'])+(np.array(data_dict['infra_num']))))*20)
    data_dict['rgb_test']=20-np.array(data_dict['infra_test'])
    new_df=pd.DataFrame(data_dict)
    new_df.to_csv(path_to_store,index=False)
    print(new_df)
if __name__ == "__main__":
    
    main()