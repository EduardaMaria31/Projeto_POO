from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.models import DBCliente
from app.schemas.cliente_schema import ClienteCreate, ClienteOut

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/", response_model=ClienteOut)
def criar_cliente(dados: ClienteCreate, db: Session = Depends(get_db)):
    cliente_existente = db.query(DBCliente).filter(DBCliente.email == dados.email).first()
    if cliente_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    novo = DBCliente(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return db.query(DBCliente).all()


@router.get("/{cliente_id}", response_model=ClienteOut)
def buscar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(DBCliente).filter(DBCliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@router.delete("/{cliente_id}")
def deletar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(DBCliente).filter(DBCliente.id == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(cliente)
    db.commit()
    return {"mensagem": "Cliente removido com sucesso"}

