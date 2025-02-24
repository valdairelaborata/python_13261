class Carro(object): 
    def __init__(self, marca, modelo, ano):        
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} - {self.modelo} - {self.ano}"

    def acelerar(self):
        return f"Acelerar o carro {self.modelo}"

    def __str__(self):
        return f"Carro ano: {self.ano}, modelo: {self.modelo}"

    def __repr__(self):
        return f"Carro(modelo={self.modelo})"

    def __del__(self):
        log = f"O objeto {self.modelo} deixou de existir"
        print("")
    
# carro = Carro("Honda", "Civic", "2003")
# carro.acelerar()
# representacao_carro = repr(carro)
# print(carro)        
# del carro

# class Numero:
#     def __init__(self, valor):
#         self.valor = valor

#     def __add__(self, outro_objeto):
#         soma_dos_objetos = self.valor + outro_objeto.valor
#         return Numero(soma_dos_objetos)

# numero1 = Numero(10)
# numero2 = Numero(20)
# resultado_da_soma = numero1 + numero2



# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def __eq__(self, outra_pessoa):
#         return self.nome == outra_pessoa.nome and self.idade == outra_pessoa.idade

#     def __ne__(self, outra_pessoa):
#         return not self.__eq__(outra_pessoa)

# pessoa1 = Pessoa("Ana", 21)
# pessoa2 = Pessoa("Ana", 21)

# sao_iguais = (pessoa1 == pessoa2)

# nao_sao_iguais = (pessoa1 != pessoa2)


class ListaPersonalizada:
    def __init__(self, itens):
        self.itens = itens
    
    def __len__(self):
        return len(self.itens)


lista = ListaPersonalizada([1,2,3,4,5])

quantos_itens_tem_na_lista = len(lista)

print("Fim")

