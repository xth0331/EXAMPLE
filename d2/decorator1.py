#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time


def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("time is %s" % (stop_time - start_time))

    return deco


def test1():
    time.sleep(4)
    print('in the test1')


def test2():
    time.sleep(3)
    print('in the test2')

print(timer(test1))
# test1 = timer(test1)
# test1()
