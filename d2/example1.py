#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 输入三个整数x,y,z，请把这三个数由小到大输出.
# x = input("x:")
# y = input("y:")
# z = input("z:")
# list = []
# if x > y:
#     list = [y,x]
#     if z > x:
#         list.append(z)
#     elif y > z:
#         list = [z,y,x]
#     else:
#         list = [y,z,x]
#
# else:   # y > x
#     list = [x,y]
#     if z > y :
#         list.append(z)
#     elif x > z :
#         list = [z,x,y]
#     else:
#         list = [x,z,y]
#
#
#
# print(list)










l = []
for i in range(3):
    number = int(input("please input your number \n"))
    l.append(number)
l.sort()
print(l)