#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('headless')
print('打开浏览器')
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get_screenshot_as_file('img\\打开浏览器截图.png')
print('输入网址：')
driver.get('https://www.baidu.com')
driver.get_screenshot_as_file('img\\输入网址截图.png')
print('输入搜索')
driver.find_element(By.ID,'kw').send_keys('sss')
driver.get_screenshot_as_file('img\\输入搜索截图.png')
print('关闭')
driver.quit()