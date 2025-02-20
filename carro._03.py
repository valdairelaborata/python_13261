
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __verificar_combustivel(self):
        print("Verificar se tem combustível")

    def acelerar(self):
        self.__verificar_combustivel()

    def frear(self):
        pass
  


carro = Carro("Honda", "Civic")
carro.acelerar()
carro.frear()

print("Fim")


