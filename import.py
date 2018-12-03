#/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
#argv 读取运行时传入参数，第一个参数为当前运行程序路径，
print(int(sys.argv[1])+int(sys.argv[2]))

#exit  退出，不理解啥意思
def exitfunc(value):
    print(value)
    sys.exit(0)
print('exit退出')
try:
    sys.exit(1)
except SystemExit:
    exitfunc(SystemExit)