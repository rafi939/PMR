# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:03:47 2022

@author: user670
"""

import socket
s=socket.socket()
print("Socket successfully created")
port=40774
s.bind(('',port))
print("socket binded to %s"%(port))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()
    print('Got connection from',addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    
    
    