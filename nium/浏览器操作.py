#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
#设置浏览器宽和高
driver.set_window_size(480,800)
#浏览器最大化
driver.maximize_window()
#浏览器最小化
# driver.minimize_window()
#设置浏览器URL---get
driver.get('https://www.baidu.com')
#获取当前地址，进行打印
print(driver.current_url)
# sleep(5)
#浏览器返回上一级
driver.back()
sleep(3)
#浏览器前进一步
driver.forward()
# driver.file_detector = 'D:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe'
#刷新页面
driver.refresh()
driver.close()
#等待多少秒，单位：秒
sleep(1)
#关闭浏览器
# driver.quit()