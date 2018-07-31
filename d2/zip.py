#!/usr/bin/env python
# -*- coding:utf-8 -*-
# keys = ['spam', 'egg', 'toast']
# vals = [1, 3, 5]
# # d3 = {}
# # for (k,v) in (zip(keys,vals)):
# #     d3[k] = v
# #
# # print(d3)
# print(dict(zip(keys, vals)))
# f = open('haproxy.cfg')
# with open('haproxy.cfg') as f:
#
#     while True:
#         line = f.readline()
#         # if not line:
#         if not line:
#             break
#         print(line, end='')
# a = [1,2,3]
# l = iter(a)
# print(l.__next__())
# print(next(l))
#
# lis = []
#
# for i in 'xyz':
#     for j in 'lmn':
#         lis.append(i+j)
#
# print(lis)
# print(sum([1,2]))
# d = {'a': 1, 'c': 3, 'b': 2}
# o = iter(d.items())
# for i,v in o:
#     print(i)
# def f1():
#     X = 88
#     def f2():
#         print(X)
#     return f2
# action = f1()
# action()
# def f1():
#     x = 99
#     def f2():
#         def f3():
#             print(x)
#         f3()
#
#     f2()
# f1()
# def tester(start):
#     state = start
#     def netsted(label):
#         nonlocal state
#         print(label,state)
#         state +=1
#     return netsted
# f = tester(0)
# f('spam')
# f('ss')



# def changer(a,b):
#     a = 2
#     b = [3,6]
#
# x = 1
# L = [1,2]
# changer(x,L)
#
# print(x,L)


# import sys
# from tkinter import Button, mainloop
# x = Button(
#         text = 'press me',
#         command = (lambda:sys.stdout.write('Spam\n')))
# x.pack()
# mainloop()
# M = [[1,2,3],[4,5,6],[7,8,9]]
# N = [[2,2,2],[3,3,3],[4,4,4]]
# test = [[M[row][col] * N[row][col] for row in range(3)] for col in range(3)]
# print(test)
# def gen(N):
#     for i in range(N):
#         yield i ** 2
#
#
# for j in gen(3):
#     print(j,end=':')
# def myzip(*seqs):
#     minlen = min(len(S) for S in seqs)
#     return [tuple(S[i] for S in seqs) for i in range(minlen)]
# S1,S2 = 'abc','xyz123'
# print(myzip(S1, S2))

#
#
# def myzip(*seqs):
#     minlen = min(len(S) for S in seqs)
#     return (tuple(S[i] for S in seqs) for i in range(minlen))
# S1,S2 = 'abc','xyz123'
# x = myzip(S1,S2)
#
#
# for i in x:
#     print(i)


def myzip(*args):
    iters = map(iter, args)

    while iters:
        res = [next(i) for i in iters ]
        yield tuple(res)


print(list(myzip('abc','lmnop')))