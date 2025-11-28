from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ======================================================
# CONFIGURAÇÃO DO BANCO DE DADOS
# ======================================================

# Caminho do banco SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./viagens.db"

# Criação do engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite + múltiplas threads
)

# Sessão do banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos ORM
Base = declarative_base()
Base.__allow_unmapped__ = True


# ======================================================
# GERENCIADOR DE SESSÃO (DEPENDÊNCIA DO FASTAPI)
# ======================================================
def get_db():
    """
    Abre uma sessão com o banco para cada requisição.
    Fecha automaticamente após a resposta.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

