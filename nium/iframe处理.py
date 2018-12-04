#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from fengzhuang import *
import re
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get('https://mail.163.com')
#for遍历所有id
for i in driver.find_elements_by_xpath("//*[@id]"):
    #通过正则匹配所有包含字符串id
    getatt = re.search('x-URS-iframe', i.get_attribute('id'))
    #非空进入
    if getatt != None:
        #赋值给变量
        x_URS = i.get_attribute('id')
# 焦点指向iframe
driver.switch_to_frame(x_URS)
# 获取Iframe中账号输入框
driver.find_element_by_name('email').send_keys('user_mail')
# 获取Iframe密码输入框
driver.find_element_by_name('password').send_keys('user_pwd')
# 通过keys模拟回车按钮
driver.find_element_by_id('dologin').send_keys(Keys.ENTER)