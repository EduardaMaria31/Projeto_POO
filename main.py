from fastapi import FastAPI
from app.Config.database import Base, engine
from app.Models.models import DBDestino, DBReserva  # importa os modelos para criar as tabelas
from app.Rotas.routers import router  # importa as rotas principais

# 🔹 Criação das tabelas no banco de dados (caso não existam)
Base.metadata.create_all(bind=engine)

# 🔹 Instância principal da aplicação FastAPI
app = FastAPI(
    title="API de Reservas de Viagens (Projeto POO)",
    description="POO - Professora Claudiany",
    version="1.0.0"
)

# 🔹 Inclui todas as rotas definidas no arquivo routers.py
app.include_router(router)

# 🔹 Endpoint raiz (página inicial)
@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API de Reservas de Viagens!"}


