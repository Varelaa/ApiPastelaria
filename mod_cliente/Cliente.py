from pydantic import BaseModel

class Cliente(BaseModel):
    id_Cliente: int = None
    nome: str
    cpf: str
    compra_fiado: int = None
    dia_fiado: int
    senha: str = None
    telefone: int