# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
from tqdm import tqdm
import pyfastcopy

def stat_count(dir):
    csv_list=os.listdir(dir)
    df_store=pd.DataFrame(columns=['Categories','Path','Frames'])
    modify_class=['misssing','wufashibei','gongzuorengyuan','qitarenyuan','konpai','gongzuorenyuan']
    modified_class=['missing','wufashibie','person','person','kongpai','person']
    drop_class=['cuowu','wufashibie','kongpai','missing']
    for csv in csv_list:
        df=pd.read_csv(dir+csv)
        for a,b in zip(modify_class,modified_class):
            df.loc[df['Categories']==a,'Categories']=b
        
        cat_list=df['Categories'].values
        
        for i,cate in enumerate(cat_list):
            if cate not in df_store['Categories'].values and cate not in drop_class:
                df_store=df_store.append([{'Categories':cate}], ignore_index=True)
                index = df_store[df_store.Categories == cate].index.tolist()[0]

                df_store.loc[index,'Path']=[df.loc[i,'Path']]
                df_store.loc[index,'Frames']=df.loc[i,'Frames']
                
            elif cate in df_store['Categories'].values and cate not in drop_class:
                index = df_store[df_store.Categories == cate].index.tolist()[0]

                df_store.loc[index,'Path']+=[df.loc[i,'Path']]
                df_store.loc[index,'Frames']+=df.loc[i,'Frames']
                
                
    df_store=df_store.sort_values(by="Frames" , ascending=False)
    df_store=df_store.reset_index().drop(['index'], axis=1)
    
    return df_store



def main():
    base='D:/mid15-dataset/'
    folder=os.listdir(base)
    image_num=0
    video_num=0
    for i in folder:
        image_num+=len(os.listdir(base+i+'/images/'))
        video_num+=len(os.listdir(base+i+'/videos/'))

    print(image_num,video_num)
    #return df_store
if __name__ == "__main__":
    main()