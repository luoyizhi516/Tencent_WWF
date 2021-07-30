import os
base='D:\WWF_Det\WWF_Data\Raw_Data/rest-all/'
cp_base=base+'-novideo/'
os.system('cp -R '+base +' '+cp_base)
folder_list=os.listdir(cp_base)
for i in folder_list:
    video_folder=cp_base+i+'/videos/'
    os.system('rm -rf '+video_folder)