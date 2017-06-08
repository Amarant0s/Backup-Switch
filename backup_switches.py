#Author=Amarant0s
from __future__ import print_function
from netmiko import ConnectHandler
import sys
import time
import select
import paramiko
import itertools
import re
old_stdout = sys.stdout
platform = 'hp_procurve'
username = 'username' # your username
password = 'password' # your password
mytime = time.strftime('%Y-%m-%d-%H-%M-%S') # To printout the date and time when the file will be created.
ip_add_file = open(r'e:\psb\ip_list2.txt','r') # a simple list of IP addresses you want to connect to each one on a new line
#loop for connecting to hosts and create backups
for host in ip_add_file:
    host = host.strip()
    filedisk = open(r'path to the backup files' + host + '-' + mytime + '.txt', 'w') #Create txt files from the ip_list.txt ip addresses. Example ('C:\Backup' + host +  + '-' + mytime + '.txt', 'w')
    sys.stdout = filedisk
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('terminal length 0')
    #output = device.send_command('show run')  
    #print('##############################################################\n')
    #print('...................CISCO COMMAND SHOW RUN OUTPUT......................\n')
    print (filedisk) #To print in the file the command that it is going to be executed.
    output = device.send_command('sh run') # The Command to run to the switch 
    print(output)
    #print('##############################################################\n')
    #print('...................CISCO COMMAND SHOW IP INT BR OUTPUT......................\n')
    #output = device.send_command('copy startup-config tftp://192.168.20.220/ + ')
    #print(output)
    #print('##############################################################\n')

filedisk.close()