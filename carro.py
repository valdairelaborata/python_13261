class Carro: 
    def __init__(self, marca, modelo, ano):        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} - {self.modelo} - {self.ano}"

    def acelerar(self):
        return f"Acelerar o carro {self.modelo}"
    
class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, ano, velocidade_maxima):
        super().__init__(marca, modelo, ano)
        self.velocidade_maxima = velocidade_maxima

    def descricao(self):
        return super().descricao() + f" {self.velocidade_maxima}"

    def  acelerar(self):
        return super().acelerar()


    
class CarroSedan(Carro):
    def __init__(self, marca, modelo, ano, tamanho_porta_malas):
        super().__init__(marca, modelo, ano)        
        self.tamanho_porta_malas = tamanho_porta_malas

    def descricao(self):
        return super().descricao() + f" {self.tamanho_porta_malas}"
   
carro_esportivo = CarroEsportivo("Honda", "Civic GTI", "2003", 250)
descricao_carro_esportivo = carro_esportivo.descricao()
carro_esportivo.acelerar()

carro_sedan = CarroSedan("Honda", "Civic", "2003", 370)
descricao_carro_sedan = carro_sedan.descricao()
carro_sedan.acelerar()

print("Fim")

