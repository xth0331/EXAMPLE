#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-26 下午4:07
# @Author   : Xieth
# @File     : adder.py
import sys

sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += int(line)
print(sum)
