import os
from nt import chdir
path = r'C:\Users\Dell\Desktop\0'+'\\man\\'+str(1)
print path
aim = r'C:\Users\Dell\Desktop\0'+'\\man\\'+str(2)
files = os.listdir(path)
i = 0
for f in files: 
    print f
    chdir(os.path.dirname(path+'\\'+f))
    os.rename(f , aim+'\\'+str(i)+'.jpg')
    i=i+1
    
