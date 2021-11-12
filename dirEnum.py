#!/usr/bin/env python

import requests,sys,math,concurrent.futures

def dir_search(dirs):

	for dir in dirs:
		sub_dir = f"http://{sys.argv[1]}/{dir}.html"
		response = requests.get(sub_dir)
		
		if response.status_code==404:
			pass
		else:
			return f"{sub_dir}     [Status code: {response.status_code}]"


if __name__=='__main__':

	if len(sys.argv)<2:
		print(f"\nUsage: python {sys.argv[0]} <ip/domain> <wordlist> <threads>")
		exit()
		
	file = open(sys.argv[2])
	dirs = file.read().split('\n')

	t = sys.argv[3]

	for i in range(math.ceil(len(dirs)/t)):
		if len(dirs)-t>t:
			pass
		else:
			t = len(dirs)-t
		with concurrent.futures.ThreadPoolExecutor() as executor:
			search = [executor.submit(dir_search, direc) for direc in dirs[i:i+t]]
			i+=t
		for res in search:
			print(res.result())

