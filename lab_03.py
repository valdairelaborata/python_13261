# Crie uma classe  com atributos titular e saldo. Adicione métodos para depositar e sacar dinheiro da conta. Certifique-se de tratar casos onde o saldo pode ser negativo.


class ContaBancaria:
        def __init__(self, titular):
                self.titular = titular
                self.saldo = 0
        
        def depositar(self, valor):
                self.saldo += valor

        def sacar(self, valor):
                self.saldo -= valor
                
        def obter_saldo(self):
                return self.saldo
                

conta_bancaria = ContaBancaria("Ana")
conta_bancaria.depositar(10)
conta_bancaria.sacar(8)

saldo = conta_bancaria.obter_saldo()

print("Fim")

