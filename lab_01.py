# 1- Considere uma classe de Conta Bancária e aplique os conceitos de encapsulamento para movimentar o saldo e a troca do titular.


class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def trocar_titular(self, novo_titular):
        self.__titular = novo_titular

    def saque(self, valor):
        self.__saldo -= valor
    
    def deposito(self, valor):
        self.__saldo += valor


conta = ContaBancaria("Ana")
conta.trocar_titular("Paulo")
conta.deposito(500)
saldo = conta.saldo
conta.saque(200)
saldo = conta.saldo
titular = conta.titular

print("")