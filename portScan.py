#!/usr/bin/env python3

import socket,sys,pyfiglet,time,concurrent.futures

# ascii_banner = pyfiglet.figlet_format("Tryhackme \nPython 4 pentesters \nScan Start")
# print(ascii_banner)



def probe_port(ip, port, result=1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip,port))
		if r==0:
			result=r
		sock.close()
	except Exception as e:
		pass
	return result


if __name__=='__main__':

	if len(sys.argv)<2:
		print("Usage: {sys.argv[0]} <ip address/domain> <port_start> <end_port>")
		exit()

	ip = sys.argv[1]
	open_ports = []
	threads = []

	ports= range(int(sys.argv[2]), int(sys.argv[3]))

	time1=time.time()

	for port in ports:
	response=probe_port(ip,port)
	if response==0:
		open_ports.append(port)

	if open_ports:
		print("Open ports: ")
		print(sorted(open_ports))
	else:
		print("All ports closed.")

	print(time.time()-time1)
