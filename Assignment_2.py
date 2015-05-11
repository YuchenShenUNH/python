#---------------------------------------------------------#
# Python Assignment 2                                     #
#                                                         #
# SECURITY SCANNER                                        #
#---------------------------------------------------------#
# Prompt user for a file name, read the file, find and    #
# report if file contains a string with "password=" in it.#
#---------------------------------------------------------#
# Author: Yuchen Shen                                     #
# 05/06/2015                                              #
#---------------------------------------------------------#
#!/usr/bin/python
import os,re

print('Assignment 2 -- SECURITY SCANNER')
print()
#file_path=input('Please input the file path: ')
file_name=input('Please input the file name to scan: ')

#if file_path.strip()=='':
file_path = os.getcwd()

print()
print('Scanning the file',file_name,'at',file_path)
print()

scan_str='password='
count=0

f = open(file_name)
for line in f.readlines():
    matched = re.findall(scan_str,line)
    if len(matched) > 0:
        count += len(matched)
f.close()
if count>0:
    print ("Found " + str(count) + " \"" + scan_str + "\"")
else:
    print ("\"" + scan_str + "\" " + "not found!")
print()
input('Scanning done! Press enter to exit...')
