#!/usr/bin/env python
# -*- coding:gbk -*-
a = "������"
print(a.encode("gbk"))
print(a.encode("utf-8"))
print(a.encode("utf-8").decode("utf-8").encode("gb2312"))
