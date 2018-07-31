#!/usr/bin/env python
# -*- coding:utf-8 -*-
import a

print(a.X, a.b.Y, a.b.c.Z)

from imp import reload

reload(a)
print(a.X, a.b.Y, a.b.c.Z)

from reloadall import reload_all

reload_all(a)
print(a.X, a.b.Y, a.b.c.Z)
