from sqlalchemy import Column, Integer, String, Date, Float
from pydantic import BaseModel
from .DataBase import Base
from datetime import date


class DBDestino(Base):
    __tablename__ = "destinos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    preco_base = Column(float)
    disponibilidade = Column(String)

class DBReserva(Base):
    __tablename__ = "reserva"
    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(String, index=True)
    destino = Column(String)
    data_viagem = Column(Date)
    num_pessoas = Column(String)
    tipo_nac_or_int = Column(String)
    preco_final = Column(float)

class DestinoCreate(BaseModel):
    nome: str
    preco_base: float
    disponibilidade: str

class ReservaCreate(BaseModel):
    id_cliente: str
    destino: str
    data_viagem: str
    num_pessoas: int
    tipo_nac_or_int: str

    class Config:
        from_attributes = True

class ReservaOut(ReservaCreate):
    id: int
    preco_final: float

