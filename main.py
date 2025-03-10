
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def Opa():
    return {"Opa!"}

@app.get("/obter-cliente")
def GetCliente():
    return {"Obter um registro de cliente!"}

@app.put("/alterar-cliente")
def PUTCliente():
    return {"Alterar um registro de cliente!"}