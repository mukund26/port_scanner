#!/usr/bin/python
#threading implemented to reduce scan time and exception handling added.
import socket, threading, os

open_port = []
closed_port = []

# function which scans the remote system for opened ports
def connScan(IP,Port):
	try:
		socket.setdefaulttimeout(7)
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((IP,Port))
		s.close()
		open_port.append(Port)
	except socket.timeout:
		closed_port.append(Port)

def main():
	
	#exception handling
  	try:
		IP= str(raw_input("[>]Input the host to be scanned: "))
		port_list = str(raw_input("[>]Enter the comma-separated list of ports to be scanned: "))
		tgtPorts = port_list.split(',')
		print tgtPorts
		if (IP == None) | (tgtPorts[0] == None):
			print '[-] You must specify a target host and port[s].'
			os._exit(1)
		print '[+]Scan starting, be patient'
		for tgtPort in tgtPorts:#create threads to thread scanner
			t=threading.Thread(target=connScan,args=(IP,int(tgtPort),))
			t.start()
		while len(open_port) + len(closed_port) != len(tgtPorts):#wait for all to complete
			continue
		print '[+]Scan finished, Results :'
		print '[*]Open ports'
		for i in open_port:#print open ports
			print '[*] '+str(i)
		print '[*]Closed ports'
		for i in closed_port:#print closed ports
			print '[*] '+str(i)
  except Exception as e:
		print '[!]Error : '+str(e)
		os._exit(1)
	
main()
