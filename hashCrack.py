#!/usr/share/env python3

import hashlib,codecs,threading,sys
from queue import Queue


# str = unicode(str, errors='ignore')

class hash_crack:
	def __init__(self, Hash, wordlist, hashtype):
		self.hash = Hash
		self.wordlist = wordlist
		self.hashtype = hashtype
		self.q = Queue()

	def hashCracker(self):
		while not self.q.empty():
			dcode = self.q.get()
			if self.hashtype.lower() == 'md5':
				hashed = hashlib.md5(dcode.encode()).hexdigest()
			elif self.hashtype.lower() == 'sha1':
				hashed = hashlib.sha1(dcode.encode()).hexdigest()
			elif self.hashtype.lower() == 'sha256':
				hashed = hashlib.sha256(dcode.encode()).hexdigest()
			elif self.hashtype.lower() == 'sha512':
				hashed = hashlib.sha512(dcode.encode()).hexdigest()

			if self.hash == hashed:
				print("Cracked: {}".format(dcode))
				sys.exit(0)

	def queue_attack(self):
		file = codecs.open(self.wordlist, 'r', encoding='utf-8', errors='ignore')
		for words in file.read().split():
			self.q.put(words)
		self.hashCracker()


	def execute(self, threads):
		thread_list = []
		for _ in range(int(threads)):
			thread = threading.Thread(target=self.queue_attack)
			thread_list.append(thread)
			thread.start()

		for thread in thread_list:
			thread.join()
					

if __name__ == "__main__":

	Usage = "Usage: python {} {} {} {}\nHashing available: MD5, SHA1, SHA256, SHA512".format(sys.argv[0],'<hash>', '<wordlist>', '<hashtype>' ' <threads(optional)>')

	if len(sys.argv)<3:
		print(Usage)
		sys.exit(0)

	hashes = ['MD5', 'SHA1', 'SHA256', 'SHA512']

	try:
		threads = sys.argv[4]
	except:
		threads=40

	if sys.argv[3].upper() not in hashes:
		print(Usage.split('\n')[1])
		sys.exit(0)
	else:
		pass
	banner = f'''
-------------------------Cracking Hashes----------------------------------
Hash: {sys.argv[1]}
Wordlist:{sys.argv[2]}
Running threads: {threads}
--------------------------------------------------------------------------
	'''


	print(banner)
	decode_hash = hash_crack(sys.argv[1], sys.argv[2], sys.argv[3])
	decode_hash.execute(threads)
