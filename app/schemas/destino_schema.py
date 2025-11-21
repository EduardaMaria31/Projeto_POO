from pydantic import BaseModel

class DestinoBase(BaseModel):
    nome: str
    preco_base: float

class DestinoCreate(DestinoBase):
    pass

class DestinoOut(DestinoBase):
    id: int

    class Config:
        orm_mode = True
