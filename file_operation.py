#/usr/bin/env python
#-*- coding:utf-8 -*-
import os

import xlrd as xlrd

paths = os.path.dirname(os.path.realpath(__file__))
print(paths+'\\text.txt')
f = open(paths+'\\text.txt','r')
d = f.readlines()
print(d[0])

files = xlrd.open_workbook('D:\\python\\text.xlsx')
table =files.sheet_by_index(0)
print( table.cell_value(0,0),table.cell_value(0,1))
