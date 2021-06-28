# -*- coding: UTF-8 -*-
import os 
import numpy as np
import cv2,argparse
def main():
    all_file='D:/check-list-part2/check-all-part2.txt'
    file_list=os.listdir('D:/check-list-part2/')
    #print(file_list)
    #file = open(all_file,'r')
    with open(all_file, 'w') as f:
        for file in file_list:
            with open('D:/check-list-part2/'+file, 'r') as f2:
                #f.write('\n')
                for i in f2:
                    f.write(i)
if __name__ == "__main__":

    main()