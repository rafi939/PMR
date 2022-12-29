# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:16:41 2022

@author: user670
"""

import psutil
network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes_sent')
bytes_recv=getattr(network_stats,'bytes_recv')
print("Bytes Sent = {0} | Bytes Received = {1}".format(bytes_sent,bytes_recv))