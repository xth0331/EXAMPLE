#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-3 下午3:02
# @Author   : Xieth
# @File     : importpandm.py

from person import Person
from manager import Manager
from decimal import *

# getcontext().prec = 6
bob = Person(name='Bob Smith', age=42, pay=Decimal(10000))
sue = Person(name='Sue Jones', age=45, pay=Decimal(20000))
tom = Manager(name='Tom Doe', age=55, pay=Decimal(30000))
db = [bob, sue, tom]
for obj in db:
    obj.giveRaise(Decimal(.10))

for obj in db:
    print(obj.lastName(), '=>', obj.pay)


