#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test1():
    print('in the test1')


def test2():
    print('in the test1')
    return 0


def test3():
    print('in the test1')
    return 1, 'hello', ['alex', 'wupeiqi'], {'name': 'alex'}


x = test1()
y = test2()
z = test3()
print(x)
print(y)
print(z)
