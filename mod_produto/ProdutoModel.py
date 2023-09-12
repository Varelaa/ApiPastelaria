import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer, BLOB
# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(10), nullable=False)
    foto = Column(BLOB, unique=True, nullable=False)
    valorUnitario = Column(CHAR(11), nullable=False)

    def __init__(self, id_produto, nome, descricao, foto, valorUnitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valorUnitario = valorUnitario