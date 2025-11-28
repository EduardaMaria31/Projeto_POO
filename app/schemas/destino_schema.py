from pydantic import BaseModel

class DestinoBase(BaseModel):
    nome: str
    preco_base: float
    descricao: str
    disponibilidade: str

class DestinoCreate(DestinoBase):
    pass

class DestinoOut(DestinoBase):
    id: int

    class Config:
        orm_mode = True
