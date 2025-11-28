from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.models import DBReserva, DBCliente, DBDestino
from app.schemas.reserva_schema import ReservaCreate, ReservaOut

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("/", response_model=ReservaOut)
def criar_reserva(dados: ReservaCreate, db: Session = Depends(get_db)):

    cliente = db.query(DBCliente).filter(DBCliente.id == dados.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    destino = db.query(DBDestino).filter(DBDestino.id == dados.destino_id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino não encontrado")

    preco_final = destino.preco_base * dados.num_pessoas

    nova_reserva = DBReserva(
        cliente_id=dados.cliente_id,
        destino_id=dados.destino_id,
        data_viagem=dados.data_viagem,
        num_pessoas=dados.num_pessoas,
        tipo_reserva=dados.tipo_reserva,
        preco_final=preco_final
    )

    db.add(nova_reserva)
    db.commit()
    db.refresh(nova_reserva)
    return nova_reserva


@router.get("/", response_model=list[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(DBReserva).all()


@router.get("/{reserva_id}", response_model=ReservaOut)
def buscar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(DBReserva).filter(DBReserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    return reserva


@router.delete("/{reserva_id}")
def deletar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(DBReserva).filter(DBReserva.id == reserva_id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    db.delete(reserva)
    db.commit()
    return {"mensagem": "Reserva removida com sucesso"}
