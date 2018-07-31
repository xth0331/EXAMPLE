#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Z = 333

def countLines(name):
    lab = []
    f = open(name, 'r')
    for i in f.readlines():
        lab.append(i)
    return len(lab)


def countChars(name):
    lab = []
    f = open(name, 'r')
    for i in f.read():
        lab.append(i)
    return len(lab)


def test(filename):
    print("This file's have %s lines" % countLines(filename))
    print("This file's have %s words" % countChars(filename))


a = input("your test filename")
test(a)
