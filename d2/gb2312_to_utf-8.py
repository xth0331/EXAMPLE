#!/usr/bin/env python
# -*- coding:gbk -*-
a = "阿萨德"
print(a.encode("gbk"))
print(a.encode("utf-8"))
print(a.encode("utf-8").decode("utf-8").encode("gb2312"))
