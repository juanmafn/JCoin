#!/usr/bin/env python3

from Block import Block

class BlockChain:
	def __init__(self):
		self.blockchain = []
		self.difficulty = 5
	
	def get_head(self):
		return self.blockchain[-1]
	
	def add(self, data):
		block = None
		if len(self.blockchain) == 0:
			block = Block(data, '0')
		else:
			block = Block(data, self.get_head().hash)
		block.mine_block(self.difficulty)
		self.blockchain.append(block)
	
	def print(self):
		for b in self.blockchain:
			b.print()
	
	def is_chain_valid(self):
		currentBlock = None
		previousBlock = None
		hashTarget = '0' * self.difficulty
		for i in range(1, len(self.blockchain)):
			currentBlock = self.blockchain[i]
			previousBlock = self.blockchain[i-1];
			# comparamos el hash registrado y el hash calculado
			if currentBlock.hash != currentBlock.calculate_hash():
				return False
			# comparamos el hash anterior con el hash anterior registrado
			if previousBlock.hash != currentBlock.previousHash:
				return False
			# comprobamos si el hash es correcto
			if currentBlock.hash[0:self.difficulty] != hashTarget:
				return False
		return True
