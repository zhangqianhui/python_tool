import os
train_data = r'D:\zhangjichao\forubuntutrain\data\train'
test_data = r'D:\zhangjichao\forubuntutrain\data\test'
#����ѵ������
train = open('D:\\test.txt' , 'w')
files = os.listdir(test_data)
for f in files:
    file_name = f.split('#' , 4)
    #���Բ���û�д��۾�
    if file_name[1] == '0' and file_name[2] == 'm':
        train.write(f+ ' 0 0\n')
    #Ů��û�д��۾�
    if file_name[1] == '0' and file_name[2] == 'f':
        train.write(f+ ' 0 1\n')
    #���Դ����۾�
    if file_name[1] == '1' and file_name[2] == 'm':
        train.write(f+ ' 1 0\n')
    #Ů�Դ����۾�
    if file_name[1] == '1' and file_name[2] == 'f':
        train.write(f+ ' 1 1\n')
    #���Դ���ī��
    if file_name[1] == '2' and file_name[2] == 'm':
        train.write(f+ ' 2 0\n')
    #Ů�Դ���ī��
    if file_name[1] == '2' and file_name[2] == 'f':
        train.write(f+ ' 2 1\n')
train.close()
