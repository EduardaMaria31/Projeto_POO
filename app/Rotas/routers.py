from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db

# MODELS ORM
from app.models.models import DBDestino, DBReserva, DBCliente

# SCHEMAS (Pydantic)
from app.schemas.destino_schema import DestinoCreate, DestinoOut
from app.schemas.reserva_schema import ReservaCreate, ReservaOut
from app.schemas.cliente_schema import ClienteCreate, ClienteOut

# SERVICE
from app.service.reserva_servico import ReservaService

# Router principal
router = APIRouter(prefix="/api", tags=["API Sistema de Reservas"])


# ===============================================================
# CLIENTES
# ===============================================================

@router.post("/clientes", response_model=ClienteOut)
def criar_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    novo = DBCliente(**cliente.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/clientes", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(DBCliente).all()


@router.delete("/clientes/{id}")
def deletar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(DBCliente).filter(DBCliente.id == id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    db.delete(cliente)
    db.commit()
    return {"mensagem": f"Cliente ID {id} removido com sucesso"}


# ===============================================================
# DESTINOS
# ===============================================================

@router.post("/destinos", response_model=DestinoOut)
def criar_destino(destino: DestinoCreate, db: Session = Depends(get_db)):
    novo = DBDestino(**destino.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/destinos", response_model=list[DestinoOut])
def listar_destinos(db: Session = Depends(get_db)):
    return db.query(DBDestino).all()


@router.delete("/destinos/{id}")
def deletar_destino(id: int, db: Session = Depends(get_db)):
    destino = db.query(DBDestino).filter(DBDestino.id == id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino não encontrado")
    db.delete(destino)
    db.commit()
    return {"mensagem": f"Destino ID {id} removido com sucesso"}


# ===============================================================
# RESERVAS
# ===============================================================

@router.post("/reservas", response_model=ReservaOut)
def criar_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    service = ReservaService(db)
    nova_reserva = service.criar_reserva(reserva)
    return nova_reserva


@router.get("/reservas", response_model=list[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(DBReserva).all()


@router.delete("/reservas/{id}")
def deletar_reserva(id: int, db: Session = Depends(get_db)):
    reserva = db.query(DBReserva).filter(DBReserva.id == id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    db.delete(reserva)
    db.commit()
    return {"mensagem": f"Reserva ID {id} removida com sucesso"}



