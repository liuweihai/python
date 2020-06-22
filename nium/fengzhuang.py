#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait():
    time.sleep(1)
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
def findSelectText(driver,id,str):
    select = Select(findId(driver,id))
    select.select_by_visible_text(str)
    return select
def findSelectValue(driver,id,str):
    select = Select(findId(driver,id))
    select.select_by_value(str)
    return select
def findSelectIndex(driver,id,str):
    select = Select(findId(driver,id))
    select.select_by_index(str)
    return select
def Login(driver):
    driver.maximize_window()
    findId(driver,'kw').send_keys('selenium')
    findId(driver,'su').click()
    findMove(driver,'tj_settingicon')
    findLinkText(driver,'搜索设置').click()
    findSelectText(driver,'nr','每页显示20条')
    findSelectValue(driver,'nr','50')
    findSelectIndex(driver,'nr',0)

#重写find_element
def find_element(self, loc):
    try:
        WebDriverWait(self.driver,15).until(lambda driver:driver.find_element(*self.loc).is_displayed())
        return self.driver.find_element(*self.loc)
    except:
        print("%s 页面未找到%s 元素" %(self,self.loc))

def zhuce(driver):
    findLinkText(driver,'登录').click()
    findLinkText(driver,'立即注册').click()
#窗口切换
def jubing(driver):
    #获取当前窗口
    handle = driver.current_window_handle
    #获取当前浏览器所有窗口  list
    handles = driver.window_handles
    print(handle)
    print('`````````````````````')
    print(handles)
    #跳转指定窗口
    driver.switch_to_window(handles[0])
    print(driver.title)
    #跳转其他窗口
    for i in handles:
        if i !=handle:
            driver.switch_to_window(i)
            print(driver.title)

