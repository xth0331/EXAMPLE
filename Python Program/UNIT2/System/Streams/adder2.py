#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-26 下午4:46
# @Author   : Xieth
# @File     : adder2.py
import sys

sum = 0
while True:
    line = sys.stdin.readline()
    if not line:
        break
    sum += int(line)
print(sum)

