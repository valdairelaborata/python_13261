import unittest

class Pessoa:
    def __init__(self, nome, idade, genero ):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def apresentar(self):
        return f"Olá, eu sou o {self.nome}, tenho {self.idade} anos e sou do gênero {self.genero}"

    # def eh_maior_de_idade(self):
    #     return self.idade >= 18


class TestePessoa(unittest.TestCase):
   
   def eh_maior_de_idade(self):
        pessoa = Pessoa("Ana", 20, "Feminino")
        eh_maior_de_idade = pessoa.eh_maior_de_idade()
        self.assertTrue(eh_maior_de_idade)
    
    # def teste_apresentar(self):
    #     pessoa = Pessoa("Ana", 20, "Feminino")
    #     apresentacao = pessoa.apresentar()
    #     # Olá, eu sou o Ana, tenho 20 anos e sou do gênero Feminino
    #     # print(apresentacao)
    #     self.assertEqual(apresentacao, "Olá, eu sou o Ana, tenho 20 anos e sou do gênero Feminino")
    
    # def eh_maior_de_idade(self):
    #     pessoa = Pessoa("Ana", 20, "Feminino")
    #     eh_maior_de_idade = pessoa.eh_maior_de_idade()
    #     self.assertTrue(eh_maior_de_idade)


unittest.main()