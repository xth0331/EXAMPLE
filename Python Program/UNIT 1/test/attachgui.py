#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter102 import MyGui

# 主窗口
mainwin = Tk()
Label(mainwin, text=__name__).pack()
# 弹出窗口
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
