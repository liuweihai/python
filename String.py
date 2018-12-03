#/usr/bin/env python
#-*- coding:utf-8 -*-
str = 'python'
print(str)  #打印字符串
print(str[0:-2])    #打印起始位置至倒数第二字符串
print(str[0])   #打印第0个下标字符串
print(str[-1])  #打印倒数第一个字符创
print(str[2:3]) #打印指定下标字符串
print(str[2:])  #打印从下标2开头的字符串
print(str*2)    #字符串乘2
print(str+'你好') #拼接字符串
print('-----------------------')    #分割线
print('Hello\nWord')    #\n  换行
print(r'Hello\nWord')   # r 打印原始字符串，不进行转义，换行

print(str,end='')