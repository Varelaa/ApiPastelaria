from pydantic import BaseModel

class Produto(BaseModel):
    id_Produto: int = None
    nome: str
    descricao: str
    valorUnitario: str
    foto: str = None