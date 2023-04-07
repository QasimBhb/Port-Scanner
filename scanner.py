#!/bin/python3

import sys
import socket
from datetime import datetime

#define target

if len(sys.argv)==2: #basically checks the amount of arguments
	target=socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("invalid amount of args")
	print("Syntax:python3 scanner.py <ip>")
	
#seperation 
print("--" * 40)
print("scanning target: "+target)
print("time started: "+str(datetime.now()))
print("--" * 40)

try:
	for port in range(0,65535):
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))
		if result==0:
			print(f"{port} is open")
		s.close()
except KeyboardInterrupt:
	print("\nExit")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
	
except socket.erro:
	print("cant connect to server")
	sys.exit() 
