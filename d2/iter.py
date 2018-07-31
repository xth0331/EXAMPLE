#!/usr/bin/env python
# -*- coding:utf-8 -*-

# def myzip(*args):
#     iters = list(map(iter, args))
#
#     while iters:
#         res = [next(i) for i in iters ]
#         yield tuple(res)
#
#
# a = (list(myzip('abc','lmnop')))
res = {}
for x in [1,2,3]:
    for y in [5,6,7]:
        res[x] = y

print(res)