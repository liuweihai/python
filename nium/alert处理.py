#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from fengzhuang import *
driver = chromes()
driver.get('D:\python\python\\nium\\test.html')
driver.find_element_by_id('pro').click()
#获取当前alert弹窗内容
ale = driver.switch_to.alert
print(ale.text)
#在弹窗中输入值
ale.send_keys('select')
#点击确定按钮
ale.accept()
#ale.dismiss()