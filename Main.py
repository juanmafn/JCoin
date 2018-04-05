#!/usr/bin/env python3

from BlockChain import BlockChain

def main():
    blockchain = BlockChain()
    
    blockchain.add('Este es el primer bloque')
    blockchain.add('Este es el segundo bloque')
    blockchain.add('Este es el tercer bloque')
    
    print('Blockchain is valid: {0}'.format(blockchain.is_chain_valid()))
    
    blockchain.print()

if __name__ == "__main__":
    main()
