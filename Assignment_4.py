#---------------------------------------------------------#
# Python Assignment 4                                     #
#                                                         #
# Pickle or Shelve user data                              #
#---------------------------------------------------------#
# Ask user to enter Name, Age and Country of Origin, then #
# use Pickle and/or Shelve to store it, write a separate  #
# function to open pickle and/or shelve and read it back. #
#---------------------------------------------------------#
# Author: Yuchen Shen                                     #
# 05/06/2015                                              #
#---------------------------------------------------------#
#!/usr/bin/python

import os,pickle,shelve

print('Assignment 4 -- Pickle or Shelve user data')
print()
Name=input('Please input the Name: ')
Age=input('Please input the Age: ')
Country=input('Please input the Country: ')

#-----------------------------
# Use pickle to store the list
#-----------------------------
f = open("pickles.txt","bw")
mylist=[Name,Age,Country]
pickle.dump(mylist,f)
f.close
#------------------------------
# re-initialize the list
#------------------------------
mylist =["c","d","e"]
print(mylist)
#-----------------------------
# Use pickle to read the list
#-----------------------------
f = open("pickles.txt","br")
mylist=pickle.load(f)
print(mylist)
f.close

input("Press enter to use the shelve to store")

s = shelve.open("A")
s[Name] = (Age,Country)
print(s[Name])
print(Name in s)
s.close()

input("Press enter to read it back with a function")
#------------------------------------------
# function to open shelve and read it back.
#------------------------------------------
def read_shelve_back(S_FileName):
    s=shelve.open(S_FileName)
    S1=(Name in s)
    s.close
    return S1
#------------------------------------------
# Open shelve and read it back.(file name is A)
#------------------------------------------
print("Note: the filename is A")
shelve_file_name = input("Please input the shelve file name: ")
print (read_shelve_back(shelve_file_name)) # read succesfule if it's true


    
