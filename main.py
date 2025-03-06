from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente

DATABASE_URL = "sqlite:///pedidos.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

novo_cliente = Cliente(nome="Ana Teste")
db.add(novo_cliente)
db.commit()




print('Opa')