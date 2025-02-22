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


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, numeroConta):
        super().__init__(titular, numeroConta)
        self.__taxa_rendimento = 0.005
    
    def render(self):
         rendimento = super().saldo * self.__taxa_rendimento
         super().deposito(rendimento)         
         
        

class ContaInvestimento(ContaBancaria):
    def __init__(self, titular, numeroConta):
        super().__init__(titular, numeroConta)
        self.__investido = 0
        self.__percentual_rendimento = 1.5
        
    @property    
    def investido(self):
        return self.__investido

    def investir(self, valor_para_investir)  :
        if valor_para_investir > 0:
            if super().saldo >= valor_para_investir:
                super().saque(valor_para_investir)
                self.__investido += valor_para_investir
    
    def resgatar(self, valor_para_resgatar):
         if valor_para_resgatar > 0:
             if self.investido >= valor_para_resgatar:
                calculo_do_rendimento = valor_para_resgatar * ( 1.5/100)
                super().deposito(valor_para_resgatar + calculo_do_rendimento)
                self.__investido -= valor_para_resgatar


conta_poupanca = ContaPoupanca("Ana", "125896")
conta_poupanca.deposito(500)
saldo = conta_poupanca.saldo
conta_poupanca.saque(100)
saldo = conta_poupanca.saldo
conta_poupanca.render()
saldo = conta_poupanca.saldo

conta_investimento = ContaInvestimento("Ana", "256387")
conta_investimento.deposito(1000)
saldo = conta_investimento.saldo
conta_investimento.saque(200)
saldo = conta_investimento.saldo
conta_investimento.investir(300)
saldo = conta_investimento.saldo
investido = conta_investimento.investido
conta_investimento.resgatar(200)
saldo = conta_investimento.saldo
conta_investimento.resgatar(200)
saldo = conta_investimento.saldo
conta_investimento.resgatar(50)
saldo = conta_investimento.saldo

