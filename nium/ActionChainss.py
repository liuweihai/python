#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
kw = driver.find_element_by_id('kw')
kw.send_keys('selenium')
#全选
kw.send_keys(Keys.CONTROL,'a')
#复制
kw.send_keys(Keys.CONTROL,'c')
#剪切
kw.send_keys(Keys.CONTROL,'x')
#粘贴
kw.send_keys(Keys.CONTROL,'v')
#回车
su = driver.find_element_by_id('su').send_keys(Keys.ENTER)
