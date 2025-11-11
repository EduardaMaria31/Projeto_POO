from sqlalchemy import Column, Integer, String, Date, Float
from app.Config.database import Base
from datetime import date
from pydantic import BaseModel

# ======================================================
# 🔹 MODELOS DO BANCO DE DADOS (SQLAlchemy ORM)
# ======================================================

class DBDestino(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    preco_base = Column(Float, nullable=False)
    disponibilidade = Column(String, nullable=False)


class DBReserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(String, index=True, nullable=False)
    destino = Column(String, nullable=False)
    data_viagem = Column(Date, default=date.today)
    num_pessoas = Column(Integer, nullable=False)
    tipo_nac_or_int = Column(String, nullable=False)
    preco_final = Column(Float, nullable=True)

# ======================================================
# 🔹 SCHEMAS (Pydantic) — usados nas rotas da API
# ======================================================

class DestinoCreate(BaseModel):
    nome: str
    preco_base: float
    disponibilidade: str

    class Config:
        from_attributes = True  # permite conversão ORM → Pydantic


class ReservaCreate(BaseModel):
    id_cliente: str
    destino: str
    data_viagem: date
    num_pessoas: int
    tipo_nac_or_int: str

    class Config:
        from_attributes = True


class ReservaOut(ReservaCreate):
    id: int
    preco_final: float



