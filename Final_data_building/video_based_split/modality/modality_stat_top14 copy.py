# -*- coding: UTF-8 -*-
import os
import pandas as pd
import shutil
import numpy as np
import cv2
from tqdm import tqdm
import pyfastcopy
import json
import imageio,skimage
from xml.etree import ElementTree
from PIL import Image, ImageDraw, ImageFont



def main():
    dataset_name='top14-all/'
    save_base='D:/WWF_Det/WWF_Det/Raw_data_stat/'+dataset_name
    df_path=save_base+'top14-all-modality.csv'
    df=pd.read_csv(df_path)
    
if __name__ == "__main__":
    main()