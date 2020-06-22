#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://news.baidu.com')
js = 'var q = document.documentElement.scrollTop = 10000'
# driver.execute_script(js)
time.sleep(3)
jss = 'var q = document.documentElement.scrollTop = 0'
# driver.execute_script(jss)
js = 'window.scrollTo(0,document.body.scrollHeight)'
driver.execute_script(js)