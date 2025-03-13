from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI

from models import Base, Cliente

app = FastAPI()

DATABASE_URL = "sqlite:///clientes.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)


class Endereco:
    def __init__(self, logradouro, bairro):
        self.logradouro = logradouro
        self.bairro = bairro




@app.get("/clientes")
def GetCliente(id: int):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    return cliente

@app.post("/clientes")
def POSTCliente(nome: str, email: str):

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    novo_cliente = Cliente(nome = nome, email=email)
    db.add(novo_cliente)
    db.commit()
    db.close()

    return {f"Cliente criado com sucesso!!!"}

@app.put("/clientes")
def PUTCliente(id: int, nome: str, email: str ):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    cliente.nome = nome
    cliente.email = email
    db.commit()
    db.close()
    return {f"Cliente {nome} alterado com sucesso!!"}

@app.delete("/clientes")
def DELETECliente(id: int):

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    db.delete(cliente)
    db.commit()
    db.close()
    return {f"Cliente {id} escluído com sucesso!!!"}