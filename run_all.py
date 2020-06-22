#/usr/bin/env python
#-*- coding:utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
import os
from tomorrow import threads
import time
#获取当前文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))
print(curpath)
#join 进入指定文件夹
casepath = os.path.join(curpath,'nium')
print(casepath)
if not os.path.exists(casepath):
    print('测试用例需要放在“case”文件夹下')
    os.mkdir(casepath)
reportpath = os.path.join(curpath,'report')
if not os.path.exists(reportpath) : os.mkdir(reportpath)

def add_test(case_path = curpath, rule = 'HelloWord*.py'):
    '''加载所有用例'''
    discover = unittest.defaultTestLoader.discover(curpath,pattern=rule,top_level_dir=None)
    return discover
@threads(1)
def run(test_suit):
    result = BeautifulReport(test_suit)
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    filename = timestr + '.html'
    result.report(filename=filename,description='自动化测试报告',log_path='report')

if __name__ == '__main__':
    cases = add_test()
    print(cases)
    for i in cases:
        print(i)
        run(i)
