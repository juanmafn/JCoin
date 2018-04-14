#!/usr/bin/env python3

from BlockChain import BlockChain
from Wallet import Wallet
from Transaction import Transaction

import StringUtil

VERBOSE = False

def test_blockchain():
    blockchain = BlockChain()

    blockchain.add('Este es el primer bloque')
    blockchain.add('Este es el segundo bloque')
    blockchain.add('Este es el tercer bloque')

    isValid = blockchain.is_chain_valid()
    if VERBOSE:
        print('Blockchain is valid: {0}'.format(isValid))
        blockchain.print()
    assert isValid, 'Blockchain ha fallado'

def test_wallet_and_signatures():
    walletA = Wallet()
    walletB = Wallet()

    # Probamos claves pública y privada
    if VERBOSE:
        print("Private and public key")
        print(StringUtil.get_string_from_key(walletA.private_key))
        print(StringUtil.get_string_from_key(walletA.public_key))

    # Creamos una transacción de pruebas de walletA a walletB
    transaction = Transaction()
    transaction.get_instance(walletA.public_key, walletB.public_key, 5, None)
    transaction.generate_signature(walletA.private_key)

    # Verificamos que la firma funciona y también desde la clave pública
    isValid = transaction.verify_signature()
    if VERBOSE:
        print(isValid)
    assert isValid, 'Firma de transacción ha fallado'

def main():
    test_blockchain()
    test_wallet_and_signatures()

if __name__ == "__main__":
    main()
