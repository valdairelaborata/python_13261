
def verifica_autenticacao(funcao):
    def autenticar():
        autenticado = True
        if(autenticado):
            funcao()
        else:
            print("Usuário não autenticado para executar!")
    return autenticar


@verifica_autenticacao
def cadastrar_produto():
    print("Aqui toda a regra para o cadastro de produto")



cadastrar_produto()


print("")