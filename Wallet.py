#!/usr/bin/env python3

class Wallet:
	def __init__(self):
		self.private_key, self.public_key = self.generate_key_pair()

	def generate_key_pair(self):
		from Crypto.PublicKey import RSA
		bits = 2048
		private_key = RSA.generate(bits, e=65537)
		public_key = private_key.publickey()
		return private_key, public_key
