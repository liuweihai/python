#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
def chromes():
    driver = webdriver.Chrome()
    return driver
def Ies():
    driver = webdriver.Ie()
    return driver
def FireFox():
    driver = webdriver.Firefox()
    return driver
def Edges():
    driver = webdriver.Edge()
    return driver

