# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:27:01 2022

@author: user670
"""

import psutil
#result01=psutil.cpu_times()
#result02=psutil.cpu_stats()
#result03=psutil.cpu_freq()
#result04=psutil.disk_partitions()
result05=psutil.net_io_counters(pernic=False)
#pernic=True --> collect all 
#print(result01)
#print(result02)
#print(result03)
#print(result04)
print(result05)
