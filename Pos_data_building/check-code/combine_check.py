# -*- coding: UTF-8 -*-
import os 
import numpy as np
import cv2,argparse
def main():
    all_file='D:/WWF_Det/WWF_Det/Drop_txt/xuebao-120-all.txt'
    file_base='D:/WWF_Det/WWF_Det/Drop_txt/xuebao-120-all/'
    file_list=os.listdir(file_base)

    with open(all_file, 'w') as f:
        for file in file_list:
            with open(file_base+file, 'r') as f2:

                for i in f2:
                    f.write(i)
if __name__ == "__main__":

    main()