#/usr/bin/env python
#-*- coding:utf-8 -*-
class Preon:
    text = u'私有值'
    def __init__(self,name):
        print(u"构造函数",name)
    def HelloWord(self):
        print("HelloWord")
    @staticmethod
    def printlf():
        print(u'私有方法')
    def __del__(self):
        print(u'析构函数')
pre = Preon('appium')
pre.HelloWord()
print(pre.text)
pre.printlf()

class A(object):
    def show(self):
        print(u'----基类')
class B(A):
    pass
class C(A):
    def show(self):
        a = A()
        a.show()
        print(u'----派生类')
class D(B,C):
    pass
d = D()
d.show()