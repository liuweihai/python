#/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from nose_parameterized import parameterized
import HTMLTestRunner
import time

class Test(unittest.TestCase):
    """演示使用"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_case1(self):
        """验证title"""
        self.assertEqual(self.driver.title,'百度一下，你就知道')

    #@unittest.skip('这条不执行')
    def test_case2(self):
        """验证URL"""
        self.assertEqual(self.driver.current_url,'https://www.baidu.com/')

    @parameterized.expand([
        ('01', 1, 2, 3),
        ('02', 2, 2, 3),
        ('03', 2, 2, 4),
        ('04', 5, 5, 10),
    ])

    def test_add(self,name,a,b,c):
        self.assertEqual(a+b,c)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(Test('test_case1'))
    suite.addTest(Test('test_case2'))
    sutest = unittest.TestCase()
    sutest.addCleanup(Test('test_add'))
    timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    filename = 'D:\\test\\result_'+timestr+'.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='自动化测试报告',description='用例执行情况',verbosity=1)
    runner.run(suite)
    fp.close()