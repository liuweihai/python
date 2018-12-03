#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import os

#获取当前driver路径
driver_path = os.path.abspath('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
os.environ["webdriver.chrome.driver"] = driver_path
#设置移动端手机类型
mobileEmulation = {"deviceName":"iPhone X"}
options = webdriver.ChromeOptions()
#屏蔽“Chrome 正受到自动测试软件的控制提示”
options.add_argument('disable-infobars')
options.add_experimental_option('mobileEmulation',mobileEmulation)
driver = webdriver.Chrome(driver_path,chrome_options=options)
driver.get('https://www.baidu.com')