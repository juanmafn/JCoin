#!/usr/bin/env python3

from time import time
from hashlib import sha256

class Block:
	def __init__(self, data, previousHash):
		self.hash = ''
		self.previousHash = ''
		self.data = ''
		self.timeStamp = 0
		self.nonce = 0
		self.__create_block(data, previousHash)
	
	def __create_block(self, data, previousHash):
		self.data = data
		self.previousHash = previousHash
		self.timeStamp = int(time() * 1000)
		self.hash = self.calculate_hash()
	
	def calculate_hash(self):
		return sha256('{0}{1}{2}{3}'.format(self.previousHash, self.timeStamp, self.nonce, self.data).encode('utf-8')).hexdigest()
	
	def mine_block(self, difficulty):
		target = '0' * difficulty
		while self.hash[0:difficulty] != target:
			self.nonce += 1
			self.hash = self.calculate_hash()
		print ('Block Mined!!! : ' + self.hash)
	
	def print(self):
		print('hash: {0}'.format(self.hash))
		print('previousHash: {0}'.format(self.previousHash))
		print('data: {0}'.format(self.data))
		print('timeStamp: {0}'.format(self.timeStamp))
		print('nonce: {0}'.format(self.nonce))
		print('----------------------------------')
