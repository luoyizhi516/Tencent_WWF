# -*- coding: UTF-8 -*-
import os 
import numpy as np
import cv2,argparse
def main():
    all_file='D:/WWF_Det/WWF_Det/Drop_txt/top14-part2-drop.txt'
    file_base='D:/WWF\data-check-list\check-list-part2/'
    file_list=os.listdir(file_base)
    #print(file_list)
    #file = open(all_file,'r')
    with open(all_file, 'w') as f:
        for file in file_list:
            with open(file_base+file, 'r') as f2:
                #f.write('\n')
                for i in f2:
                    f.write(i)
if __name__ == "__main__":

    main()