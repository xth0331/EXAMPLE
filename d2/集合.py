#!/usr/bin/env python
# -*- coding:utf-8 -*-
# f = open("test.txt", 'r')
# count = 0
# for line in f:
#     count +=1
#     if count == 9:
#         print('test--------')
#         continue
#     print(line)


# f = open("test.txt", 'r')
# count = 0
# for line in f:
#     if count == 9:
#         print('test--------')
#         count += 1
#         continue
#     print(line)
#     count += 1
# f = open("test.txt", 'r')
# print(f.tell() )#文件指针
# print(f.readline())
# print(f.readline())
# print(f.tell())
# f.seek(0)
# print(f.tell())
# import sys, time
#
# for i in range(22):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.2)
# f = open("test.txt", 'r+',encoding="utf-8") # 读写
# f = open("test.txt", 'w+', encoding="utf-8")  # 写读
# f.write("------------------diao--------------\n")
# f.write("------------------diao--------------\n")
# f.write("------------------diao--------------\n")
# f.write("------------------diao--------------\n")
# f.write("------)
# print(f.readline())
# f.write("second line ")
# f.close()
f = open("yesterday2", "r", encoding="utf-8")
f_new = open("yesterday2.bak", "w", encoding="utf-8")


for line in f:
    if "成千个我所做过的梦" in line:
        line = line.replace("成千个我所做过的梦","成千个alex所做过的梦")
    f_new.write(line)

f.close()
f_new.close()


