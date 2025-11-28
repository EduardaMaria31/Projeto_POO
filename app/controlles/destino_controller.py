from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.models import DBDestino
from app.schemas.destino_schema import DestinoCreate, DestinoOut

router = APIRouter(prefix="/destinos", tags=["Destinos"])


@router.post("/", response_model=DestinoOut)
def criar_destino(dados: DestinoCreate, db: Session = Depends(get_db)):
    nome_existente = db.query(DBDestino).filter(DBDestino.nome == dados.nome).first()
    if nome_existente:
        raise HTTPException(status_code=400, detail="Destino já cadastrado")

    novo = DBDestino(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/", response_model=list[DestinoOut])
def listar_destinos(db: Session = Depends(get_db)):
    return db.query(DBDestino).all()


@router.get("/{destino_id}", response_model=DestinoOut)
def buscar_destino(destino_id: int, db: Session = Depends(get_db)):
    destino = db.query(DBDestino).filter(DBDestino.id == destino_id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino não encontrado")
    return destino


@router.delete("/{destino_id}")
def deletar_destino(destino_id: int, db: Session = Depends(get_db)):
    destino = db.query(DBDestino).filter(DBDestino.id == destino_id).first()
    if not destino:
        raise HTTPException(status_code=404, detail="Destino não encontrado")

    db.delete(destino)
    db.commit()
    return {"mensagem": "Destino removido com sucesso"}
