#!/usr/bin/env python3

from hashlib import sha256
import StringUtil

class Transaction:
    def __init__(self):
        # Hash de la transacción
        self.transaction_id = None
        # Clave pública del emisor
        self.sender = None
        # Clave pública del recibidor/beneficiario
        self.recipient = None
        # Cantidad de la transacción
        self.value = 0
        # Firma para evitar que otros gasten fondos de nuestra wallet
        self.signature = None

        # Transacciones entrantes
        self.inputs = []
        # Transacciones salientes
        self.outputs = []

        # Número de transacciones generadas
        self.sequence = 0

    def get_instance(self, _from, to, value, inputs):
        self.sender = _from
        self.recipient = to
        self.value = value
        self.inputs = inputs

    def calculate_hash(self):
        self.sequence += 1
        s = '{0}{1}{2}{3}'.format(
            StringUtil.get_string_from_key(self.sender),
            StringUtil.get_string_from_key(self.recipient),
            self.value,
            self.sequence)
        return sha256(s.encode('utf-8')).hexdigest()

    def generate_signature(self, private_key):
        data = '{0}{1}{2}'.format(
            StringUtil.get_string_from_key(self.sender),
            StringUtil.get_string_from_key(self.recipient),
            self.value)
        self.signature = StringUtil.apply_sig(private_key, data)

    def verify_signature(self):
        data = '{0}{1}{2}'.format(
            StringUtil.get_string_from_key(self.sender),
            StringUtil.get_string_from_key(self.recipient),
            self.value)
        return StringUtil.verify_sig(self.sender, data, self.signature)