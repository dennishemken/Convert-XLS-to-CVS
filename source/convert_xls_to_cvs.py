# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 10:44:49 2017

@author: saamu
"""
#import os
from os import listdir
from os.path import splitext
import pyexcel as pe

def convert_xlsx_to_csv(filename):
    book = pe.get_book(file_name=filename + ".xlsx")
    
    book

    book.save_as(filename + ".csv")
    print("File Converted.")
    return

directory = listdir('.')

filelist = []
for x in directory:
    print(splitext(x))
    if splitext(x)[1] == ".xlsx":
        filelist.append(splitext(x)[0])
        
for filename in filelist:
    convert_xlsx_to_csv(filename)
    
print("All files converted")