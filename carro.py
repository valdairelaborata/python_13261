class Carro: 
    def __init__(self, cor, placa, status, tipo):        
        self.cor = cor
        self.placa = placa
        self.status = status
        self.tipo = tipo
    
    def vender(self):
        self.status = "Vendido"

    def ligar(self):
        self.status = "Ligado"

    def desligar(self):
        self.status = "Desligado"

    def acelerar_frente(self):
        pass

    

carro = Carro("Preta", "AKS-2563", "Desligado", "Hatch")
carro.ligar()
carro.desligar()


print("Fim")

