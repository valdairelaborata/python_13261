import requests

def obter_endereco_pelo_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta_via_cep = requests.get(url)
    
    if(resposta_via_cep.status_code == 200):
        dados = resposta_via_cep.json()
        print(f"Logradouro : {dados['logradouro']}")
        print(f"Bairro : {dados['bairro']}")
        


obter_endereco_pelo_cep("81580010")

