#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
class Browser():
    def chromes(self):
        driver = webdriver.Chrome()
        return driver
    def Ies(self):
        driver = webdriver.Ie()
        return driver
    def FireFox(self):
        driver = webdriver.Firefox()
        return driver

