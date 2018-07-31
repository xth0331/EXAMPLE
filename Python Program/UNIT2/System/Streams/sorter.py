#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-26 下午4:03
# @Author   : Xieth
# @File     : sorter.py
import sys

lines = sys.stdin.readlines()
lines.sort()
for line in lines:
    print(line, end='')
