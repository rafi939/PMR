# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:11:54 2022

@author: user670
"""
"""
import ifaddr
adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("IPs of network adapter "+adapter.nice_name)
    for ip in adapter.ips:
        print(" %s/%s" %(ip.ip,ip.network_prefix))"""
''' 
if you wish to include network interfaces that do not hsve ip/configured then,pass param'''
import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IPs of network adapter "+adapter.nice_name)
    if(adapter.ips):
        for ip in adapter.ips:
           print(" %s/%s" %(ip.ip,ip.network_prefix))
    else:
        print(" No IPs configured")
        