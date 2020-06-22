#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
from nium import fengzhuang,Browser
import unittest
import time

class Test_Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Browser.chromes()
    def setUp(self):
        self.driver.get('D:\python\\nium\\test.html')

    def test_01(self):
        self.alt = fengzhuang.findId(self.driver,'alt')
        self.assertEqual(self.alt.get_attribute('value'),'alert')

    def test_02(self):
        self.ck1 = fengzhuang.findId(self.driver,'test1')
        self.ck1.click()
        self.assertEqual(fengzhuang.findId(self.driver,'test1').is_selected(), 'True')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()