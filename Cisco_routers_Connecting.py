from netmiko import ConnectHandler
with open('device.txt') as router:
    for IP in router:
        Router={
       "device_type":"cisco_ios",
       "ip":"sandbox-iosxe-recomm-1.cisco.com",
       "port":22,
       "username":"developer",
       "password":"C1sco12345"  
          }
        net_connect=ConnectHandler(**Router)
        print('Connecting to ' +IP)
        print('-'*79)
        output=net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()
