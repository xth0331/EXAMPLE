#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-3 下午5:49
# @Author   : Xieth
# @File     : test.py
def isqrt(n):
    i = int(math.sqrt(n) + 0.5)
    if i**2 == n:
        return i
    raise ValueError('input was not a perfect square')