#!/usr/bin/python
# -*- coding: UTF-8 -*-
year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))
months1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #闰年
months2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年
sumday = 0
if (year % 4 == 0) and (year % 100 != 0)  or (year % 400 == 0 ) :
    sumday = months1[(month-1)] + day
else:
    sumday = months2[(month-1)] + day

print("this date is this year's %s day" %sumday)