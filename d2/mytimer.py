#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import time
#
# reps = 1000
# repslist = range(reps)
#
#
# def timer(func, *pargs, **kwargs):
#     start = time.clock()
#     for i in repslist:
#         ret = func(*pargs, **kwargs)
#         elapsed = time.clock() - start
#         return (elapsed, ret)
import sys
import time

if sys.platform[:3] == "win":
    timefunc = time.clock
else:
    timefunc = time.time


def trace(*args): pass


def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)
    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
        elapsed = timefunc() - start
        return (elapsed, ret)


def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best:
            best = time
    return (best, ret)
