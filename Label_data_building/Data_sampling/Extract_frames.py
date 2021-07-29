
import PIL.Image as Image
from pandas.core import base
import pylab
import imageio
import skimage
import numpy as np
import os
from subprocess import DETACHED_PROCESS, call
from tqdm import tqdm
import pandas as pd
import argparse
def extract_frames(src_path,target_path):
    
    new_path = target_path
 
    for video_name in tqdm(os.listdir(src_path)):
        
        filename = src_path +'/' +video_name
        #print(filename)
        cur_new_path = new_path+'/'+video_name.split('.')[0]
        
        # if not os.path.exists(cur_new_path):
        #     os.mkdir(cur_new_path)
        dest = cur_new_path +'-%04d.jpg'
        #print(dest)
        os.system("ffmpeg" + " -i" +' ' +filename +" -r" +" 1" +' '+ dest)
        #os.system("ffmpeg" + " -i" +' ' +filename +" -r" +" 0.5" +' -q:v 2 -f image2'+' '+ dest)
def main():
    base,start,end=opt.base,opt.start,opt.end
    for i in os.listdir(base):
        cate_folder=os.path.join(base,i)
        video_folder=os.path.join(cate_folder,'videos')
        frame_folder=os.path.join(cate_folder,'frames')
        if not os.path.exists(frame_folder):
            os.makedirs(frame_folder)
        
        extract_frames(video_folder,frame_folder)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', type=str, default=r'D:\WWF_Det\WWF_Data\Raw_Data\top14-p10/', help='dataset_store_dir')
    parser.add_argument('--start', type=int, default=0, help='start_folder')
    parser.add_argument('--end', type=int, default=15, help='end_folder')


    opt = parser.parse_args()
    main()