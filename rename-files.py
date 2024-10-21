#!/usr/bin/python3

import os

path = os.path.dirname('/home/marcus/projects/tests/')

files = os.listdir(path)

os.chdir(path)

for file in files:
    file_name = file
    new_file = file_name.lower()
    final_file = new_file.replace(' ', '-')
    os.rename(file, final_file)
    print(final_file)
