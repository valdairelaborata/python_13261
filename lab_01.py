import unittest

class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0
    
    @property
    def saldo(self):
        return self.__saldo
        
    def saque(self, valor):
        self.__saldo -= valor 

    def deposito(self, valor):
        self.__saldo += valor 

class TesteContaBancaria(unittest.TestCase):

    def teste_deposito(self):
        conta_bancaria = ContaBancaria("Ana")
        conta_bancaria.deposito(50)
        self.assertEqual(50, conta_bancaria.saldo)

    def teste_saque(self):
        conta_bancaria = ContaBancaria("Ana")
        conta_bancaria.deposito(150)
        saldo_anterior = conta_bancaria.saldo
        conta_bancaria.saque(60)
        self.assertEqual(saldo_anterior - 60, conta_bancaria.saldo)        



unittest.main()

 