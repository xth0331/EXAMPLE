#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-3 下午2:40
# @Author   : Xieth
# @File     : manager.py
from person import Person
from decimal import *

class Manager(Person):
    def giveRaise(self, percent, bouns=Decimal(.10)):
        self.pay *= (Decimal(1.0) + percent + bouns)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=Decimal(50000))
    print(tom.lastName())
    tom.giveRaise(Decimal(.20))
    print(tom.pay)
