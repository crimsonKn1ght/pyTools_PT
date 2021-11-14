#!/usr/share/env python3

import socket
import threading
import sys
from queue import Queue

class portDiscovery:

	def __init__(self):
		self.q = Queue()
		# self.open_ports=[]

	def portScan(self,ip, port):
		try:
			scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			scan.settimeout(1.5)
			scan.connect((ip, port))
			return True
		except:
			return False

	def get_ports(self,ports):
		for port in range(int(ports)):
			self.q.put(port)

	def worker(self):
		while not self.q.empty():
			port = self.q.get()
			if self.portScan(sys.argv[1], port):
				open_ports.append(port)
				print('[+] Open port: {}'.format(port))
			else:
				pass

	def run_scan(self,threads):
		self.get_ports(sys.argv[2])
		thread_list = []
		
		for _ in range(int(threads)):
			thread = threading.Thread(target=self.worker)
			thread.start()
			thread_list.append(thread)

		for thread in thread_list:
			thread.join()

class bannerGrabber:

	def __init__(self):
		pass

	def bannerDisplay(self):
		for port in open_ports:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(10)
			try:
				sock.connect((sys.argv[1], port))
				banner = sock.recv(1024)
				print("Port {}: banner".format(port))
			except:
				print("Port {}: Couldn\'t retrieve banner".format(port))



if __name__=='__main__':

	if len(sys.argv)<2:
		print("Usage: python portScanner <ip-address> <	ports>")
		sys.exit(0)

	open_ports = []

	print('--------Starting syn scan--------')
	portDisc = portDiscovery()
	portDisc.run_scan(300)

	banners = bannerGrabber()
	banners.bannerDisplay()
