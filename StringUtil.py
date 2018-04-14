#!/usr/bin/env python3

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
# from Crypto.PublicKey import RSA

def apply_sig(private_key, input):
    digest = SHA256.new()
    digest.update(input.encode('utf-8'))
    signer = PKCS1_v1_5.new(private_key)
    return signer.sign(digest)

def verify_sig(private_key, data, signature):
    verifier = PKCS1_v1_5.new(private_key.publickey())
    digest = SHA256.new()
    digest.update(data.encode('utf-8'))
    return verifier.verify(digest, signature)

def get_string_from_key(key):
    return key.exportKey().hex()