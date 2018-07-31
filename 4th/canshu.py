#!/usr/bin/env python
# -*- coding:utf-8 -*-
# def adder(*args):
#     if type(args[0]) == type(0):
#         sum = 0
#     else:
#         sum = args[0][:0]
#     for i in args:
#         sum = sum + i
#     return sum
#
#
#
#
# def adder2(*args):
#     sum = args[0]
#     for x in args[1:]:
#         sum +=x
#     return sum
#


# print(adder2([1,2,3],[7,8,9]))


# def adder3(good=1,bad=2,ugly=3):
#     return good + bad + ugly
#
# print(adder3(bad=77,good=1))

# def adder(**args):
#     argskeys = list(args.keys())
#     tot = args[argskeys[0]]
#     for key in argskeys[1:]:
#         tot += args[key]
#     return tot


# def adder1(*args):
#     tot = args[0]
#     for arg in args[1:]:
#         tot +=arg
#     return tot

# def adder2(**args):
#     args = list(args.values())
#     tot = args[0]
#     for arg in args:
#         tot +=arg
#     return tot


# def adder3(**args):
#     return adder1(*args.values())
# print(adder3(a=9,b=10,c=100,d=1000))

# def copyDict(old):
#     new = {}
#     for key in old.keys():
#         new[key] = old[key]
#     return new
#
#
# print(copyDict({'a':11,'b':22}))
# def addDict(dict1,dict2):
#     new = {}
#     for key in dict1.keys():
#         new[key] = dict1[key]
#     for key in dict2.keys():
#         new[key] = dict2[key]
#     return new
#
#
#
# print(addDict({'a':1,'b':2},{'b':2,'c':4}))
# def f1(a, b):
#     print(a, b)
#
#
# def f2(a, *b):
#     print(a, b)
#
#
# def f3(a, **b):
#     print(a, b)
#
#
# def f4(a, *b, **c):
#     print(a, b, c)
#
#
# def f5(a, b=2, c=3):
#     print(a, b, c)
#
#
# def f6(a, b=2, *c):
#     print(a, b, c)


# f1(1, 2) # true 1,2
# f1(b=2, a=1) # true 1,2
# f2(1, 2, 3)  # *args 传入元祖
# f3(1, x=2, y=3) # 字典
# f4(1, 2, 3, x=2, y=3) # 1 (2,3) {'x':2,'y':3}
# f5(1) # 1 2 3
# f5(1, 4) #1 4 3
# f6(1) # 1 2 ()
# f6(1, 3, 4) # 1 3 (4)
#


# year = int(input("Please input year"))
# if type(year) == int:
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('This year is runnian')
#     else:
#         print('no')
#
y = 4
x = y // 2 # 2
while x > 1: # 2 > 1
    if y % x == 0: # 4 % 2 == 0
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')


