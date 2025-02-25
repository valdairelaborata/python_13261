# Crie uma classe chamada ContaBancaria que represente uma conta bancária básica. A conta deve ter um número de conta,
# um titular da conta e um saldo.
class ContaBancaria:
 
# Implemente os seguintes métodos mágicos:
# __init__(self, numero, titular, saldo): O construtor que inicializa os atributos da conta.
# __str__(self): O método que retorna uma representação em string da conta no formato "Conta de [titular]: [saldo]".
    def __init__(self, conta, titular, saldo):
        self.numero = conta
        self.titular = titular
        self.saldo = saldo
 
    def __str__(self):
        return f"Conta de {self.titular}: {self.saldo}"
 
# Além dos métodos mágicos, implemente também os seguintes métodos:
# depositar(self, valor): Adiciona um valor ao saldo da conta.
# sacar(self, valor): Retira um valor do saldo da conta, desde que haja saldo suficiente..
 
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Realizado o depósito no valor de {valor}.")
        else:
            print("O valor a ser depositado deve positivo.")
 
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Realizado o saque no valor de {valor}.")
        else:
            print("Saldo insuficiente.")
   
# Criando o objeto da ContaBacaria
conta = ContaBancaria("99.999-99", "Nelsiellen Buisa", 5000)
print(conta)  
conta.depositar(500)
print(conta)
conta.sacar(200)
print(conta)  
conta.sacar(1500)
 