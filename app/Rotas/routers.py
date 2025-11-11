from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.Config.database import get_db
from app.Models import DBDestino, DBReserva, DestinoCreate, ReservaCreate, ReservaOut
from datetime import date

router = APIRouter(prefix="/api", tags=["Reservas e Destinos"])

# ========================================
# 🔹 ROTAS DE DESTINOS
# ========================================

@router.post("/destinos", response_model=DestinoCreate)
def criar_destino(destino: DestinoCreate, db: Session = Depends(get_db)):
    """Cria um novo destino no banco"""
    db_destino = DBDestino(**destino.dict())
    db.add(db_destino)
    db.commit()
    db.refresh(db_destino)
    return db_destino


@router.get("/destinos")
def listar_destinos(db: Session = Depends(get_db)):
    """Lista todos os destinos"""
    destinos = db.query(DBDestino).all()
    return destinos


@router.delete("/destinos/{id}")
def deletar_destino(id: int, db: Session = Depends(get_db)):
    """Deleta um destino pelo ID"""
    destino = db.query(DBDestino).filter(DBDestino.id == id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino não encontrado")
    db.delete(destino)
    db.commit()
    return {"mensagem": f"Destino ID {id} removido com sucesso"}

# ========================================
# 🔹 ROTAS DE RESERVAS
# ========================================

@router.post("/reservas", response_model=ReservaOut)
def criar_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    """Cria uma nova reserva e calcula o preço final"""
    # Busca o destino selecionado
    destino = db.query(DBDestino).filter(DBDestino.nome == reserva.destino).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino não encontrado")

    # Cálculo simples do preço final
    preco_final = destino.preco_base * reserva.num_pessoas

    nova_reserva = DBReserva(
        id_cliente=reserva.id_cliente,
        destino=reserva.destino,
        data_viagem=reserva.data_viagem,
        num_pessoas=reserva.num_pessoas,
        tipo_nac_or_int=reserva.tipo_nac_or_int,
        preco_final=preco_final
    )

    db.add(nova_reserva)
    db.commit()
    db.refresh(nova_reserva)
    return nova_reserva


@router.get("/reservas")
def listar_reservas(db: Session = Depends(get_db)):
    """Lista todas as reservas"""
    reservas = db.query(DBReserva).all()
    return reservas


@router.delete("/reservas/{id}")
def deletar_reserva(id: int, db: Session = Depends(get_db)):
    """Deleta uma reserva pelo ID"""
    reserva = db.query(DBReserva).filter(DBReserva.id == id).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")
    db.delete(reserva)
    db.commit()
    return {"mensagem": f"Reserva ID {id} removida com sucesso"}

