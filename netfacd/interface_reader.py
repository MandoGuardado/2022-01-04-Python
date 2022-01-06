#!/usr/bin/env python3
import netifaces
print(netifaces.interfaces())
def mac_request(i):
    return (netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']

def ip_request(i):
    return (netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']



for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('Mac: ', end='')
            print(mac_request(i))
            print('IP: ', end='')
            print(ip_request(i))
        except:
            print("Could not collect adapter information") # print an error message

