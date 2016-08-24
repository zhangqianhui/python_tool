import os
train_data = r'D:\zhangjichao\forubuntutrain\data\train'
test_data = r'D:\zhangjichao\forubuntutrain\data\test'
#对于训练数据
train = open('D:\\test.txt' , 'w')
files = os.listdir(test_data)
for f in files:
    file_name = f.split('#' , 4)
    #男性并且没有戴眼镜
    if file_name[1] == '0' and file_name[2] == 'm':
        train.write(f+ ' 0 0\n')
    #女性没有戴眼镜
    if file_name[1] == '0' and file_name[2] == 'f':
        train.write(f+ ' 0 1\n')
    #男性带了眼镜
    if file_name[1] == '1' and file_name[2] == 'm':
        train.write(f+ ' 1 0\n')
    #女性带了眼镜
    if file_name[1] == '1' and file_name[2] == 'f':
        train.write(f+ ' 1 1\n')
    #男性带了墨镜
    if file_name[1] == '2' and file_name[2] == 'm':
        train.write(f+ ' 2 0\n')
    #女性带了墨镜
    if file_name[1] == '2' and file_name[2] == 'f':
        train.write(f+ ' 2 1\n')
train.close()
