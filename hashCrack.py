#!/usr/share/env python3

import hashlib,codecs


# str = unicode(str, errors='ignore')

class hash_crack:
	def __init__(self):
		self.hash = input("Type in the hash: ")
		self.wordlist='/usr/share/wordlists/rockyou.txt'
		self.hashCracker()

	def hashCracker(self):
		with codecs.open(self.wordlist, 'r', encoding='utf-8', errors='ignore') as file:
			for line in file.readlines():
				hashed = hashlib.md5(line.strip().encode()).hexdigest()
				if self.hash == hashed:
					print(line.strip())
					break
					

if __name__ == "__main__":
	hashcode = hash_crack()
	# print("Password found:", hashcode)
