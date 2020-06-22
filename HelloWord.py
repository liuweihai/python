# /usr/bin/env python
# -*- coding:utf-8 -*-
import csv
import time

import xlrd
from selenium import webdriver
import unittest
import os
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# @ddt
class TestCase(unittest.TestCase):
    def find_element(self, loc):
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print("%s 页面未找到%s 元素" % (self, loc))
    #重写clear_keys
    def clear_keys(self, loc):
        self.find_element(loc).clear()
    #重写send_keys
    def send_keys(self, loc, value):
        self.clear_keys(loc)
        self.find_element(loc).send_keys(value)
    #重写click
    def click_button(self, loc):
        self.find_element(loc).click()
    #页面打开首次运行
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def Login(self, username, password):
        user_name = (By.ID, 'TANGRAM__PSP_10__userName')
        user_pwd = (By.ID, 'TANGRAM__PSP_10__password')
        user_click = (By.ID, 'TANGRAM__PSP_10__submit')
        self.send_keys(user_name, username)
        self.send_keys(user_pwd, password)
        self.click_button(user_click)

    #创建数据
    # @data(('123456', ''),('l714053171','liuGang0\s.'))
    # #解压元祖
    # @unpack
    def readfile(self,index):
        f = open('D:\\python\\text.txt','r')
        d = f.readlines()
        f.close()
        return d[index]
    #获取xlsx  文件，注意都是数值类型需要转换
    def filexmlx(self, rowvalue, colvalue):
        word = xlrd.open_workbook('d:\\python\\text.xlsx')
        tables = word.sheet_by_index(0)
        return tables.cell_value(rowvalue,colvalue)
    def filecsv(self,value1,value2):
        csvs = open('d:\\python\\text.csv','r')
        reader = csv.reader(csvs)
        data = []
        for row in reader:
            data.append(row)
        csvs.close()
        print(data[value1][value2])
        return data[value1][value2]

    def test_case1(self):
        login_button = (By.LINK_TEXT, '登录')
        user_button = (By.ID, 'TANGRAM__PSP_10__footerULoginBtn')
        user_error = (By.ID, 'TANGRAM__PSP_10__error')
        self.click_button(login_button)
        self.find_element(user_button).click()
        # self.Login(self.filexmlx(0,0),self.filexmlx(0,1))
        self.Login(self.filecsv(1,0),self.filecsv(1,1))
        text_text = self.find_element(user_error).text
        self.assertEqual(text_text, '请您输入密码')
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()
