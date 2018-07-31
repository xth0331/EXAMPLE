#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 18-7-3 下午2:17
# @Author   : Xieth
# @File     : person.py
from decimal import *
getcontext().prec = 6
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (Decimal(1.0) + percent)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, Decimal(30000), 'software')
    sue = Person('Sue Jones', 45, Decimal(40000), 'hardware')
    print(bob.name, sue.pay)
    print(bob.lastName())
    sue.giveRaise(Decimal(.10))
    print(sue.pay)
