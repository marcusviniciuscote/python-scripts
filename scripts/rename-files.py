#!/usr/bin/python3

import os

enter_path = str(input('Enter the entire path to rename the files: ')).strip()

path = os.path.dirname(enter_path)

files = os.listdir(path)

os.chdir(path)

for file in files:
    file_name = file
    new_file = file_name.lower()
    final_file = new_file.replace(' ', '-')
    os.rename(file, final_file)
    print(final_file)
