from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.reserva_schema import ReservaCreate, ReservaOut
from app.service.reserva_servico import ReservaService
from app.models.models import DBReserva

router = APIRouter(prefix="/reservas", tags=["Reservas"])


# ======================================================
#  CRIAR RESERVA (USANDO O SERVICE)
# ======================================================
@router.post("/", response_model=ReservaOut)
def criar_reserva(dados: ReservaCreate, db: Session = Depends(get_db)):
    service = ReservaService(db)           # <-- INSTANCIA O SERVICE
    resultado = service.criar_reserva(dados)  # <-- CHAMA O MÉTODO CORRETO

    if isinstance(resultado, dict) and "erro" in resultado:
        raise HTTPException(status_code=400, detail=resultado["erro"])

    return resultado


# ======================================================
#  LISTAR RESERVAS
# ======================================================
@router.get("/", response_model=list[ReservaOut])
def listar_reservas(db: Session = Depends(get_db)):
    return db.query(DBReserva).all()


# ======================================================
#  BUSCAR RESERVA POR ID
# ======================================================
@router.get("/{reserva_id}", response_model=ReservaOut)
def buscar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(DBReserva).filter(DBReserva.id == reserva_id).first()

    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    return reserva


# ======================================================
#  DELETAR RESERVA
# ======================================================
@router.delete("/{reserva_id}")
def deletar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(DBReserva).filter(DBReserva.id == reserva_id).first()

    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    db.delete(reserva)
    db.commit()

    return {"mensagem": "Reserva removida com sucesso"}

