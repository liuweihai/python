#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from fengzhuang import *
driver = chromes()
driver.get('https://www.baidu.com')
Login(driver)
