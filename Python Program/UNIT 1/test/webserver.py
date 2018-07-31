#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python实现一个HTTP WEB 服务器，他知道如何运行服务器端CGI脚本,
从当前工作目录提供的文件和脚本，Python脚本必须存储在webdir\cgi-bin或webdir\htbin中
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'  # 存放HTML文件和cgi-bin脚本文件夹的所在
port = 8888  # 缺省http://localhost/,也可以使用 http://localhosy:xxx/
os.chdir(webdir)  # 在HTML根目录中运行
srvraddr = ("", port)  # 我的主机名和端口号
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()  # 以永久地守护进程运行
