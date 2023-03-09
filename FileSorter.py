import os
import shutil

from_dir = 'C:/Users/pangp/Downloads'
to_dir = 'C:/Users/pangp/OneDrive/Desktop/Document_Files'
list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)
    string = f'{name} {extension}'

    print(string)