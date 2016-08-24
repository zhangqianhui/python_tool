import os
man_path = r'D:\zhangjichao\data_argu_8_15\gender_pre\gender_pre\test\0'
woman_path = r'D:\zhangjichao\data_argu_8_15\gender_pre\gender_pre\test\1'

lines = open('D:\\test_filename.txt')
for line in lines:
    line=line.strip('\n')
    file = man_path + '\\' + line
    print file
    if os.path.exists(file):
        m_file = line.split('.jpg' , 1)[0]
        os.rename(file , man_path + '\\' + m_file + '#1#.jpg')
    else:
        print file
        file = woman_path + '\\' + line
        m_file = line.split('.jpg' , 1)[0]
        os.rename(file , woman_path + '\\' + m_file + '#1#.jpg')
lines.close()

lines = open('D:\\test_filename2.txt' , 'r')
for line in lines:
    line=line.strip('\n')
    file = man_path + '\\' + line
    if os.path.exists(file):
        m_file = line.split('.jpg' , 1)[0]
        os.rename(file , man_path + '\\' + m_file + '#0#.jpg')
    else:
        print file
        file = woman_path + '\\' + line
        m_file = line.split('.jpg' , 1)[0]
        os.rename(file , woman_path + '\\' + m_file + '#0#.jpg')
lines.close()

lines = open('D:\\test_filename3.txt' , 'r')
for line in lines:
    line=line.strip('\n')
    file = man_path + '\\' + line
    if os.path.exists(file):
        m_file = line.split('.jpg' , 1)[0]
        os.rename(file , man_path + '\\' + m_file + '#2#.jpg')
    else:
        print file
        file = woman_path + '\\' + line
        m_file = line.split('.jpg' , 1)[0]
        os.rename(file , woman_path + '\\' + m_file + '#2#.jpg')
lines.close()
