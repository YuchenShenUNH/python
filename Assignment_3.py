#---------------------------------------------------------#
# Python Assignment 3                                     #
#                                                         #
# HOW MUCH OPERATION ON A DICTIONARY IS FASTER            #
# THAN OPERATION ON A SHELVE?                             #
#---------------------------------------------------------#
# Use following to time your code. Do similar operations  #
# on a dictionary and shelve with same data in them and   #
# document which one is faster.                           #
# from datetime import datetime                           #
# dt1 = datetime.now()                                    #
#---------------------------------------------------------#
# Author: Yuchen Shen                                     #
# 05/06/2015                                              #
#---------------------------------------------------------#
#!/usr/bin/python
import os,shelve
from datetime import datetime

print('Assignment 3')
print('------------')
print('Compare OPERATION ON A DICTIONARY and OPERATION ON A SHELVE')
print()
#---------------------------------------------
# Creates an empty English to Frech dictionary
#---------------------------------------------
en_to_fr={}
#---------------------------------------------
# Store 5 entries in the dictionary
#---------------------------------------------
en_to_fr['hello'] = 'bonjour'
en_to_fr['world'] = 'monde'
en_to_fr['red'] = 'rouge'
en_to_fr['green'] = 'vert'
en_to_fr['blue'] = 'bleu'

#---------------------------------------------
# Creates a shelve file to store the same thing
#---------------------------------------------
s = shelve.open("English_French")
s['hello'] = ('bonjour')
s['world'] = ('monde')
s['red'] = ('rouge')
s['green'] = ('vert')
s['blue'] = ('bleu')
#print(s['hello'])
#print('hello' in s)
s.close()

#---------------------------------------------------
# Operation on dictionary: print all entries 10 times 
#---------------------------------------------------
input('Press Enter to start operation on dictionary') 
dt1 = datetime.now() # get the current time
print("Operation on dictionary: print all entries 10 times")
for i in range(0,10):
    print(en_to_fr['hello'],en_to_fr['world'])
    print("red is",en_to_fr['red'])
    print("green is",en_to_fr['green'])
    print("blue is",en_to_fr['blue'])
    print()   
dt2 = datetime.now()
print ('Dictionary operation time elapsed:', dt2-dt1)
print ()

#---------------------------------------------------
# Operation on shelve: print all entries 10 times 
#---------------------------------------------------
input('Press Enter to start operation on shelve') 
print()
print("Operation on shelve: print all entries 10 times")
dt1 = datetime.now()
s = shelve.open("English_French")
for i in range(0,10):
    print(s['hello'],s['world'])
    print("red is",s['red'])
    print("green is",s['green'])
    print("blue is",s['blue'])
    print()
dt2 = datetime.now()
print ('Shelve operation time elapsed:', dt2-dt1)
print()
s.close
input('Press enter to exit...')
