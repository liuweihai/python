#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
def wait():
    time.sleep(2)
def findId(driver,id):
    wait()
    d = driver.find_element_by_id(id)
    return d
def findName(driver,name):
    wait()
    d = driver.find_element_by_name()
    return d
def findxPath(deiver,Xpath):
    wait()
    d = driver.find_element_by_xpath(Xpath)
    return d
def findClassName(driver,ClassName):
    wait()
    d = driver.find_element_by_class_name(ClassName)
    return d
def findLinkText(driver,LinkText):
    wait()
    d = driver.find_element_by_link_text(LinkText)
    return d
def findMove(driver,Move):
    sele = driver.find_element_by_name(Move)
    ActionChains(driver).move_to_element(sele).perform()

def Login(driver):
    findId(driver,'kw').send_keys('selenium')
    findId(driver,'su').click()
    findMove(driver,'tj_settingicon')
def chromes():
    driver = webdriver.Chrome()
    return driver
def Ies():
    driver = webdriver.Ie()
    return driver
