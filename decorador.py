
def meu_decorador(funcao):
    def wrapper():
        print("Antes da funcão")
        funcao()
        print("Depois da função")
    return wrapper


@meu_decorador
def minha_funcao():
    print("Minha função")


minha_funcao()


print("")