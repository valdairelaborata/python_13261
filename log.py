def log_decorador(funcao):
    def log():
        print(f"A funcão {funcao} está sendo iniciada")
        funcao()
        print(f"A funcão {funcao} está sendo finalizada")
    return log


@log_decorador
def adicionar_registro():
    print("Aqui vamos adicionar o registro no banco.")

@log_decorador
def alterar_registro():
    print("Aqui vamos alterar o registro no banco.")

@log_decorador
def excluir_registro():
    print("Aqui vamos excluir o registro no banco.")


excluir_registro()
adicionar_registro()
alterar_registro()



print("")