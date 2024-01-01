import pyfiglet
import sys
import socket
import ipaddress
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


with open('ip.txt', 'r') as f:
	for line  in f:
				ip = line.strip()
				# print(ip)
				if ipaddress.ip_address(ip):
					target= socket.gethostbyname(ip)
					print(target)
					print("-" * 50)
					print("Scanning Target: " + target)
					print("Scanning started at:" + str(datetime.now()))
					print("-" * 50)
					try:
					# will scan ports between 1 to 65,535
						for port in range(1,65535):
							s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
							socket.setdefaulttimeout(1)
					
					# returns an error indicator
							result = s.connect_ex((target,port))
							if result == 0:
								print("Port {} is open".format(port))
							# else:
							# 	print("Port {} is closed".format(port))
							s.close()
					
					except KeyboardInterrupt:
							print("\n Exiting Program !!!!")
							sys.exit()
					except socket.gaierror:
							print("\n Hostname Could Not Be Resolved !!!!")
							sys.exit()
					except socket.error:
							print("\ Server not responding !!!!")
							sys.exit()
			






