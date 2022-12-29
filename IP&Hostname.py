# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:35:39 2022

@author: user670
"""

import socket
hostname=socket.gethostname()
print(socket.gethostname())
ipadd=socket.gethostbyname(hostname)
print(ipadd)
print(socket.gethostbyaddr(ipadd))