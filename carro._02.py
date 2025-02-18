
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__velocidade = 0

    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, valor):
         self.__velocidade += valor

    def acelerar(self):
        self.velocidade += 5

    def frear(self):
        self.__velocidade -= 5
  


carro = Carro("Honda", "Civic")
velocidade_do_carro = carro.velocidade
carro.acelerar()
velocidade_do_carro = carro.velocidade
carro.frear()
velocidade_do_carro = carro.velocidade
carro.acelerar()
velocidade_do_carro = carro.velocidade
carro.acelerar()
velocidade_do_carro = carro.velocidade

print("Fim")

