
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from lab_01 import Base, Cliente

# DATABASE_URL = "sqlite:///sql_alchemy.db"
# engine = create_engine(DATABASE_URL)

# Base.metadata.create_all(bind=engine)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# db = SessionLocal()

# # novo_cliente = Cliente(nome = "Paulo", email="paulo@gmail.com")
# # db.add(novo_cliente)
# # db.commit()

# # clientes = db.query(Cliente).all()

# # for cliente in clientes:
# #     print(f"Nome: {cliente.nome} - E-mail: {cliente.email}")


# # select * from cliente c where c.id = 2

# cliente = db.query(Cliente).filter(Cliente.id == 2).first()
# cliente.nome = "Claudio"
# cliente.email = "claudio@gmail.com"


# cliente = db.query(Cliente).filter(Cliente.id == 2).first()
# db.delete(cliente)
# db.commit()


# db.close()