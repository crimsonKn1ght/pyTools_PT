#!/usr/bin/env python

import requests,sys,threading
from queue import Queue

class dirScanner:
	def __init__(self, ip, wordlist, ext, threads):
		self.ip = ip
		self.wordlist = wordlist
		self.ext = ext
		self.threads = threads
		self.q = Queue()

	def dirScan(self):
		while not self.q.empty():
			dir = self.q.get()
			url = f"http://{self.ip}/{dir}.{self.ext}"
			response = requests.get(url, verify=False)
			
			if response.status_code==404:
				pass
			else:
				directories.append(url)
				print(url,"                [Status code:",response.status_code,"]")

	def dirEnum(self):
		file = open(self.wordlist, 'r')
		for dir in file.read().split():
			self.q.put(dir)

		thread_list = []

		for _ in range(int(self.threads)):
			thread = threading.Thread(target=self.dirScan)
			thread_list.append(thread)
			thread.start()

		for thread in thread_list:
			thread.join()


if __name__=='__main__':

	if len(sys.argv)<4:
		print("Usage: python dir_enum.py <ip-address> <wordlist> <extension> <threads>")
		sys.exit(0)

	directories = []

	scan = dirScanner(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	scan.dirEnum()
