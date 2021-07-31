# -*- coding: UTF-8 -*-
import os 
import numpy as np
import cv2,argparse
def main():
    base,txt_path,start,end=opt.img_dir,opt.text_dir,opt.start,opt.end
    img_list=os.listdir(base)
    
    txt_path=r'D:\WWF_Det\WWF_Det\Drop_txt\top14-part7/check3100-3200.txt'
    with open(txt_path, 'w') as f:

        for i in img_list[3100:3200]:
            img_dir=base+i
            print(img_dir)
            
            img=cv2.imread(img_dir)
            win_name=img_dir
            cv2.namedWindow(win_name,0)
            cv2.resizeWindow(win_name, 1024, 720)
            cv2.imshow(win_name,img)
            k=cv2.waitKey(0)
            if k & 0xFF == ord('y'):
                cv2.destroyAllWindows()
                continue
            elif k & 0xFF == ord('n'):
                f.write(os.path.splitext(i)[0]+'\n')
                cv2.destroyAllWindows()

                continue
            elif k & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir', type=str, default=r'D:\WWF_Det\WWF_Data\Pos_Data\top14-part7\allset\visualizations/', help='dataset_store_dir')
    parser.add_argument('--text_dir', type=str, default='check.txt', help='result')
    parser.add_argument('--start', type=int, default='0', help='start_img')
    parser.add_argument('--end', type=int, default='3210', help='start_img')
    opt = parser.parse_args()
    main()