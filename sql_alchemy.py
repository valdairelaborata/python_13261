
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lab_01 import Base, Cliente

DATABASE_URL = "sqlite:///sql_alchemy.db"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

novo_cliente = Cliente(nome = "Paulo", email="paulo@gmail.com")
db.add(novo_cliente)
db.commit()

db.close()