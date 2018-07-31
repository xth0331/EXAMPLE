#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from decimal import *
getcontext().prec = 6
db = shelve.open('class-shelve')
sue = db['sue']
sue.giveRaise(Decimal(.25))
db['sue'] = sue
tom = db['tom']
tom.giveRaise(Decimal(.20))
db['tom'] = tom
db.close()
