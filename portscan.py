#!/bin/python3

import socket
from sys import argv
import os
from time import sleep


args = argv
open_ports = []

def show_help():
	print(f"""
	______________________________
	|                            |
	|                            |
	|        PORT SCANNER        |
	|                            |
	|                            |
	- Author: @marcos.dev.web

    USAGE:

      ./{os.path.basename(__file__)} www.example.com <80 || ports.txt>


""")
	exit()
                           
try:
	url = str(args[1])
except:
	show_help()

if url in '--help':
	show_help()
else:
	try:
		ports = str(args[2])
	except:
		show_help()

	if ports in '--help':
		show_help()

if os.path.isfile(ports):
	try:
		with open(ports, 'r') as f:
			ports = [i for i in f.read().split('\n') if len(i) > 0]
			f.close()
	except:
		print(f'Error to open file "{ports}"')
		exit()
else:
	if ports.isnumeric():
		ports = [ports]
	else:
		print('You need pass or a port or a file with list of ports')
		exit()




os.system('clear')

print('[***] Scanning ports...')
sleep(2)


for port in ports:
	os.system('clear')
	if port.isnumeric():
		addr = (url, int(port))
	else:
		print(f'Invalid value inside list: [{port}]')
		exit()

	try:
		print(f'[+] Scanning port [{port}]')
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(3)
		response = sock.connect_ex(addr)
		if response == 0:
			open_ports.append(port)
	except socket.timeout:
		continue

os.system('clear')

if len(open_ports) > 1:
	print(f'-------------------- OPEN PORTS --------------------')
	print()
	c = 0
	for port in open_ports:
		if c < 5:
			print(port, end=' | ')
		else:
			print()
			print(port, end=' | ')
			c = 0
		c += 1
	print('\n')
else:
	if len(open_ports) == 0:
		print('\Not port is open!\n')
		exit()
	else:
		for port in open_ports:
			print(f'OPEN: {port}')
	print()
