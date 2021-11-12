#!/usr/share/env python3

#This code will be modified shortly so that it can also 
#grab banners for ports, even tho a small change of sock.recv(1024)
#would be enough, I'm not sure how good itwork with threading

import socket,threading,sys
from queue import Queue

class portScanner:
	def __init__(self, target):
		self.target = target
		self.open_ports=[]

	def portscan(self, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((self.target, port))
			return 1
		except:
			return 0

	def portArrange(self, sport, eport):
		self.q = Queue()
		for port in range(int(sport),int(eport)+1):
			self.q.put(port)

	def worker(self):
		while not self.q.empty():
			port = self.q.get()
			if self.portscan==1:
				print(f'[+] Port {port} is open')
				self.open_ports.append(port)
			else:
				pass

	def run_scan(self, threads):
		self.portArrange(sys.argv[2], sys.argv[3])
		thread_list=[]

		for _ in range(int(threads)):
			thread = threading.Thread(target=self.worker)
			thread_list.append(thread)

		for thread in thread_list:
			thread.start()
	
		for thread in thread_list:
			thread.join()

if __name__=='__main__':
	
	if len(sys.argv)<3:
		print("Usage: {sys.argv[0]} <ip-address> <start-port> <end-port> <threads(optional)>")
		exit()

	t=20
	if sys.argv[4]:
		t=sys.argv[3]

	scan = portScanner(sys.argv[1])
	scan.run_scan(t)
