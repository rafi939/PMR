# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 11:16:21 2022

@author: user670
"""

from socket import getservbyname, getservbyport
a=getservbyname("ssh") 
b=getservbyport(22)
print(a) 
print(b)