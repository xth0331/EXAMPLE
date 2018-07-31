#!/usr/bin/env python
# -*- coding:utf-8 -*-
#*args 接受位置参数 转换成元组形式  **kwargs 接受关键字参数  转换字典形式
# def test2(**kwargs):
#     print(kwargs['name'])
#
#
# def test3(*args):
#     print(args)



def test4(name, *args, **kwargs):
    print(name)
    print(kwargs)


test4('alex', age=19, sex='m')
#
# test3(1,2,3)
#
#
# test2(name='alex',age=8,sex='F')
#
