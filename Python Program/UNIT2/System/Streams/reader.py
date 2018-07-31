#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-26 下午3:02
# @Author   : Xieth
# @File     : reader.py


print('Got this : "%s"' % input())
import sys

data = sys.stdin.readline()[:-1]
print('The meaning of life is ', data, int(data) * 2)
