from pydantic import BaseModel
from datetime import date

class ReservaBase(BaseModel):
    id_cliente: int
    destino: str
    data_viagem: date
    num_pessoas: int
    tipo_nac_or_int: str

class ReservaCreate(ReservaBase):
    pass

class ReservaOut(ReservaBase):
    id: int
    preco_final: float

    class Config:
        orm_mode = True
