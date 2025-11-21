from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base
from datetime import date

# ======================================================
# MODELO CLIENTE
# ======================================================

class DBCliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefone = Column(String, nullable=False)

    reservas = relationship("DBReserva", back_populates="cliente")


# ======================================================
# MODELO DESTINO
# ======================================================

class DBDestino(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True, nullable=False)
    preco_base = Column(Float, nullable=False)
    disponibilidade = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    reservas = relationship("DBReserva", back_populates="destino_rel")


# ======================================================
# MODELO RESERVA
# ======================================================

class DBReserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    destino_id = Column(Integer, ForeignKey("destinos.id"), nullable=False)

    data_viagem = Column(Date, default=date.today)
    num_pessoas = Column(Integer, nullable=False)

    tipo_reserva = Column(String, nullable=False)  # nacional | internacional
    preco_final = Column(Float, nullable=True)

    cliente = relationship("DBCliente", back_populates="reservas")
    destino_rel = relationship("DBDestino", back_populates="reservas")


