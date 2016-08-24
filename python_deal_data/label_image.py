import os
man_path = r'D:\zhangjichao\data_argu_8_15\gender_pre\gender_pre\test\0'
woman_path = r'D:\zhangjichao\data_argu_8_15\gender_pre\gender_pre\test\1'
print man_path
files = os.listdir(man_path)
for f in files:
    file_name = f.split('.jpg' , 1)[0]
    os.rename(man_path + '\\' + f , man_path + '\\' + file_name+'m#.jpg')
files = os.listdir(woman_path)
for f in files:
    file_name = f.split('.jpg' , 1)[0]
    os.rename(woman_path + '\\' + f , woman_path + '\\' + file_name+'f#.jpg')


    
