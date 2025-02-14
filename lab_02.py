# 2 - Crie uma classe Calculadora com métodos para adição, subtração, multiplicação e divisão. Crie uma instância da classe e realize algumas operações.

class Calculadora: 
    def __init__(self, resultado = 0):
        self.resultado = resultado

    def adicao(self, valor):
        self.resultado += valor

    def subtracao(self, valor):
        self.resultado -= valor
    
    def multiplicacao(self, valor):
        self.resultado *= valor

    def divisao(self, valor):
        self.resultado /= valor
    
    def exibir_resultado(self):
        return self.resultado


calculadora = Calculadora()

calculadora.adicao(10)
calculadora.adicao(5)
calculadora.subtracao(15)
calculadora.adicao(50)
calculadora.divisao(5)
calculadora.multiplicacao(2)

resultado = calculadora.exibir_resultado()


print("Fim")