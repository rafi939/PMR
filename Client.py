# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:57:29 2022

@author: user670
"""

import socket
s=socket.socket()
port=40674
s.connect(('127.0.0.1',port))
print(s.recv(1024).decode())
s.close()