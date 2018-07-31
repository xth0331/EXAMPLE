#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
分割字符串或文本文件并交互分页
"""


def more(text, numlines=15):
    lines = text.splitlines()  # 效果类似split('\n'),不过不用在末尾加''
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys  # 运行时进行此操作，导入不进行

    more(open(sys.argv[1]).read())
