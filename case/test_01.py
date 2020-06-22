#/usr/bin/env python
#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import unittest
@unittest.skip
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    def setUp(self):
        self.driver.get('https://www.baidu.com/')
    def test_01(self):
        '''用例一：验证title'''
        self.assertEqual(self.driver.title,'百度一下，你就知道')
        self.assertIn('百度一下，你就知道',self.driver.title)
    def test_02(self):
        '''用例二：验证URL'''
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()