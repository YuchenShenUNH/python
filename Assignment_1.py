#-----------------------------------------------------#
# Python Assignment 1                                 #
#                                                     #
# File Finder                                         #
#-----------------------------------------------------#
# Prompt user to enter a start path and file name,    #
# search recursively for the given file name starting #
# at the given path, when file is found, display the  #
# full path to the file.                              #
#-----------------------------------------------------#
# Auther: Yuchen Shen                                 #
# 05/06/2015                                          #
#-----------------------------------------------------#
#!/usr/bin/python

import os
import fnmatch

print('Please enter the start path and the file name you want to search.')
start_path=input('The start path: ')
file_name=input('The file name: ')
print()
print('Searching the file',file_name,'starting at',start_path)
print()
for dirpath, dirs, files in os.walk(start_path):
    for single_file in files:
        if fnmatch.fnmatch(single_file, file_name):
            print("Found",single_file,"at",dirpath)
print()
input('Search done! Press enter to exit...')






