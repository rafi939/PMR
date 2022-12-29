# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 14:34:10 2022

@author: user670
"""

import socket
addr = '127.0.0.25'
try:
    socket.inet_aton(addr)
    print("Valid IP")
except socket.error:
    print("Invalid IP")
    
'''
import os,ipaddress
os.system('cls') # os.system will clear the console at the start of excution
while(True):
    ip=input("enter ip address: ")
    try:
        print(ipaddress.ip_address(ip))
        print('IP Valid')
    except:
        print('-' *50)
        print('Ip is not valid')
    finally:
        if(ip=='mango'):
            print('Script Finished')
            break
'''