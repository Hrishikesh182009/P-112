import os
import shutil

from_dir = 'C:/Users/Admin/Downloads'
to_dir = 'C:/Users/Admin/Documents/Documents_Files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for ele in list_of_files:
    source,ext = os.path.splitext(ele)
    if ext == '':
        pass
    if ext in['.txt', '.pdf', '.doc', '.docx']:
        path1 = from_dir + '/' + ele
        path2 = to_dir
        path3 = to_dir + '/' + ele
        print(path1)
        print(path2)

        if os.path.exists(path2):
            print('Moving' + ele)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Moving'+ ele )
            shutil.move(path1,path3)
