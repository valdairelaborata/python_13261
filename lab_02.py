# 2 - Crie uma classe ContaBancaria que inclui funcionalidades básicas e uma classe ContaCorrente que herda da classe base. A classe derivada ContaCorrente substitui o método sacar para considerar um limite de saque além do saldo disponível.

class ContaBancaria:
    def __init__(self, titular, numeroConta):
        self.__titular = titular
        self.__numeroConta = numeroConta
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
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, numeroConta, limite):
        super().__init__(titular, numeroConta)
        self.__limite = limite
   
    @property
    def limite(self):
        return self.__limite
 
    def saque(self, valor_do_saque):

       if self.saldo >= valor_do_saque:
            super().saque(valor_do_saque)
       else:
           print("Saldo insuficiente para o saque")
    
    @property
    def saldo(self):
        return super().saldo + self.limite


conta_corrente = ContaCorrente("Atila", "501025", 500)
conta_corrente.deposito(500)
saldo = conta_corrente.saldo
conta_corrente.trocar_titular("Ana")
titular = conta_corrente.titular
conta_corrente.saque(600)
saldo = conta_corrente.saldo
conta_corrente.saque(500)
conta_corrente.deposito(150)
conta_corrente.saque(500)
saldo = conta_corrente.saldo
 
print(f"seu novo saldo é ")
 