
from fastapi import FastAPI
import requests

app = FastAPI()

class Endereco:
    def __init__(self, logradouro, bairro):
        self.logradouro = logradouro
        self.bairro = bairro


@app.get("/consulta-cep")
def Opa(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta_via_cep = requests.get(url)

    if(resposta_via_cep.status_code == 200):
        dados = resposta_via_cep.json()
        endereco = Endereco(logradouro = dados['logradouro'], bairro=dados['bairro'])
        return endereco
    else:
        return {"Consulta via cep com erro!"}



# @app.get("/obter-cliente")
# def GetCliente():
#     return {f"Obter um registro de cliente!{id}"}

# @app.put("/alterar-cliente")
# def PUTCliente():
#     return {"Alterar um registro de cliente!"}