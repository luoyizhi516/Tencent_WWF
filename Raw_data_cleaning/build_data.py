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
    modify_class=['misssing','wufashibei','gongzuorengyuan','qitarenyuan','konpai','gongzuorenyuan','hongzuiya']
    modified_class=['missing','wufashibie','person','person','kongpai','person','hongzuishanya']
    #drop_class=['cuowu','wufashibie','kongpai','missing','banchunlu','yanyang:konpai']
    drop_class=['cuowu','wufashibie','missing','banchunlu','yanyang:konpai']

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
                #['[path]', '[path2]','[path3]']

                df_store.loc[index,'Path']+=[df.loc[i,'Path']]
                df_store.loc[index,'Frames']+=df.loc[i,'Frames']
                
                
    df_store=df_store.sort_values(by="Frames" , ascending=False)
    df_store=df_store.reset_index().drop(['index'], axis=1)
    
    return df_store



def main():
    new_df=stat_count('F:\All_CSV\csv/')[:1]
    print(new_df)
    for cate,file_list in tqdm(zip(new_df['Categories'].values,new_df['Path'].values)):
        image_folder='D:/WWF_Det/WWF_Data/Raw_Data/'+cate+'/images/'
        video_folder='D:/WWF_Det/WWF_Data/Raw_Data/'+cate+'/videos/'
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        if not os.path.exists(video_folder):
            os.makedirs(video_folder)
        count_image=0
        count_video=0
        
        for mini_list in tqdm(file_list):
            source_list=mini_list[1:-1].split(',')
            for s_item in source_list:
                source=s_item.strip()[1:-1]
                if source.lower().strip().endswith('.jpg') or source.lower().strip().endswith('.png') :
                    count_image+=1
                    target=image_folder+'%05d' % (count_image) +os.path.splitext(source)[1]
                    if not os.path.exists(target):
                        source=source.replace('E:','F:\Raw_Dataset',1)
                        shutil.copyfile(source,target)
                        k=0
                elif source.lower().strip().endswith('.mov') or source.lower().strip().endswith('.avi') or source.lower().strip().endswith('.mp4'):
                    count_video+=1
                    target=video_folder+'%05d' % (count_video) +os.path.splitext(source)[1]
                    if not os.path.exists(target):
                        source=source.replace('E:','F:\Raw_Dataset',1)
                        shutil.copyfile(source,target)
                        k=0
                else:
                    print((os.path.splitext(source)[1])[-3:])
                
                #shutil.copyfile(source,target)
                #print(target)
   
if __name__ == "__main__":
    main()