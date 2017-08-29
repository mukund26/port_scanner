#!/usr/bin/python
import socket
from socket import *

# function which scans the remote system for opened ports
def connScan(IP,Port):
    try:
       	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((IP,Port))
	s.close()
        print '[+]...............tcp Port %d is open'%Port
        
    except:
        print '[-]...............tcp Port %d is closed'%Port


IP= str(raw_input("Input the host to be scanned: "))
port_list = str(raw_input("Enter the comma seperated list of ports to be scanned: "))
tgtPorts = port_list.split(',')
print tgtPorts

if (IP == None) | (tgtPorts[0] == None):
	print '[-] You must specify a target host and port[s].'
        exit(0)

for tgtPort in tgtPorts:
	print 'Scanning port :',tgtPort
	connScan(IP, int(tgtPort))
			
