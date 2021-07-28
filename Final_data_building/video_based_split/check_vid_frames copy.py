import cv2
#获取一个视频并打开
cap=cv2.VideoCapture("D:/WWF_Det/WWF_Data/Final_Data/valset-vid-v1/gaoyuantu/00143.AVI")

if cap.isOpened():  #VideoCaputre对象是否成功打开
    print('已经打开了视频文件')
    fps = cap.get(cv2.CAP_PROP_FPS)  # 返回视频的fps--帧率
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 返回视频的宽
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 返回视频的高
    frames=cap.get(7)
    print('fps:', fps,'width:',width,'height:',height,frames)
    i=0
    while 1:
            i=i+1
            ret, frame = cap.read()  # 读取一帧视频
            # ret 读取了数据就返回True,没有读取数据(已到尾部)就返回False
            # frame 返回读取的视频数据--一帧数据
            file_name='D:\WWF_Det\WWF_Data\Final_Data\gaoyuantu-frame/'+str(i)+'.jpg'
            cv2.imwrite(file_name, frame)


else:
    print('视频文件打开失败')