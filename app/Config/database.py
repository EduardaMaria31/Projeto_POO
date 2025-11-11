from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com o banco de dados (usando SQLite local)
SQLALCHEMY_DATABASE_URL = "sqlite:///./viagens.db"

# Criação do "motor" que faz a conexão com o banco
# O parâmetro connect_args é necessário apenas para SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Criação da sessão (conexão temporária com o banco)
SessionLocal = sessionmaker(
    autocommit=False,  # exige commit manual (segurança)
    autoflush=False,   # evita flush automático antes das queries
    bind=engine
)

# Base que servirá de herança para os modelos ORM
Base = declarative_base()
Base.__allow_unmapped__ = True  # permite classes com anotações antigas (SQLAlchemy 2.0+)

# Dependência usada no FastAPI para abrir e fechar a sessão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()