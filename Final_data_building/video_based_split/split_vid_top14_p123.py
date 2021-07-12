# -*- coding: UTF-8 -*-
from math import e, inf
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
        #test
        data_stat_path='D:\WWF_Det\WWF_Det\Raw_data_stat/top14-p1-p2-p3-merged/top14-p123-combine.csv'
        critiria_path='D:/WWF_Det/WWF_Det/Raw_data_stat/top14-all/split_critiria.csv'
        save_base='D:/WWF_Det/WWF_Det/Final_data_stat/top14-p123/'
        if not os.path.exists(save_base): os.makedirs(save_base)
        save_path=save_base+'video_split.csv'
        df=pd.read_csv(data_stat_path)
        df['label']=None
        id_list=df.index.values.tolist()
        df_cri=pd.read_csv(critiria_path)
        cate_list=np.unique(df['cate'].values)
        np.random.seed(2021)
        
        for cate in cate_list:
            
            infra_index=df.loc[(df['cate'] == cate)&(df['modality'] == 'Infra')].sample(frac=1).index.values.tolist()
            rgb_index=df.loc[(df['cate'] == cate)&(df['modality'] == 'RGB')].sample(frac=1).index.values.tolist()
            infra_test_num=int(df_cri.loc[df_cri['cate']==cate]['infra_test'])
            rgb_test_num=int(df_cri.loc[df_cri['cate']==cate]['rgb_test'])
            infra_test_index=infra_index[:infra_test_num]
            rgb_test_index=rgb_index[:rgb_test_num]

            test_index_all=list(infra_test_index+rgb_test_index)
            
            train_index_all=[i for i in infra_index+rgb_index if i not in test_index_all]
            #print(len(test_index_all))
            for ID in test_index_all:
            
                df.loc[ID,'label']='test'
                ori_dir=df.loc[ID,'video_path']
                cate=df.loc[ID,'cate']
                target_base=os.path.join('D:/WWF_Det/WWF_Data/Final_Data/valset-vid-v1/',cate)
                target_dir=os.path.join(target_base,ori_dir.split('/')[-1])
                if not os.path.exists(target_base): os.makedirs(target_base)
                shutil.copyfile(ori_dir,target_dir)
            for ID in train_index_all:
                df.loc[ID,'label']='train'
            #print(df)
            #break
        # df.to_csv(save_path,index=False)

if __name__ == "__main__":
    
    main()