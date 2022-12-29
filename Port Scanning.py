# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 14:15:30 2022

@author: user670
"""

import socket
import subprocess
import sys
from datetime import datetime
#subprocess.call('clear',shell=Time)
remoteServer=input("Enter a remote host to scan : ")
remoteServerIP=socket.gethostbyname(remoteServer)
print("_"*60)
print("PLease wait,scanning remote host ",remoteServerIP)
print("_"*60)
t1=datetime.now()
print(t1)
try:
    for port in range(1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        print(result)
        if(result==0):
            print("Port {}:      Open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could no be resolved. Existing")
    sys.close()
except socket.error:
    print("Could't connect server")
    sys.exit()
