import os
base='D:\WWF_Det\WWF_Data\Raw_Data/rest-p2'
cp_base=base+'-novideo/'
os.system('cp -R '+base +' '+cp_base)
folder_list=os.listdir(cp_base)
print(cp_base)
for i in folder_list:
    video_folder=cp_base+i+'/images/'
    os.system('rm -rf '+video_folder)