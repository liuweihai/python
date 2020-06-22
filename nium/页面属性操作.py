#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select,WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
#引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
import  os
options = webdriver.ChromeOptions()
#关闭浏览器自动化控制
options.add_argument('disable-infobars')
#浏览器启动时最大化
options.add_argument('-start-maximized')
#打开浏览器
driver = webdriver.Chrome(chrome_options=options,)
#跳转制定页面
driver.get('https://www.baidu.com')
#获取百度输入框，send_keys进行输入
driver.find_element_by_id("kw").send_keys('selenium')
#获取搜索按钮，点击
driver.find_element_by_id('su').click()
#等待时间
# sleep(3)
#获取当前页面源码
# driver.page_source
#获取当前调试工具
driver.name
#获取link_text，进行点击操作
#driver.find_element_by_link_text('百度首页').click()
#通过name属性，获取指定元素
select = driver.find_element_by_name('tj_settingicon')
#通过ActionChains获取当前容器，进行鼠标停留到指定元素，perfrom进行执行操作
ActionChains(driver).move_to_element(select).perform()
#获取xpath路径，打开设置---高级搜索页面
driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[2]').click()
#关闭高级搜索
cla = driver.find_element_by_xpath('//*[@id="wrapper"]/div[7]/span')
cla.click()
pass
driver.find_element_by_link_text('登录').click()
print(driver.current_url)
sleep(3)
driver.find_element_by_link_text('立即注册').click()
print(driver.current_url)
