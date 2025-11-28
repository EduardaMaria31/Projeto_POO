from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import Base, engine

# ROTAS
from app.controlles.cliente_controller import router as cliente_router
from app.controlles.destino_controller import router as destino_router
from app.controlles.reserva_controller import router as reserva_router


# ============================================================
#  🔧 BANCO DE DADOS – cria as tabelas automaticamente
# ============================================================
Base.metadata.create_all(bind=engine)


# ============================================================
#  🚀 CONFIGURAÇÃO DA APLICAÇÃO FASTAPI
# ============================================================
app = FastAPI(
    title="API de Reservas de Viagens ✈️",
    version="2.0.0",
    description=(
        "API educacional desenvolvida para demonstrar conceitos de **POO**, "
        "**camadas de serviço**, **CRUD completo**, **SQLAlchemy ORM** e "
        "arquitetura organizada com FastAPI.\n\n"
        "➡️ Permite cadastrar clientes, destinos e criar reservas "
        "nacionais ou internacionais com cálculo automático de preço."
    ),
    contact={
        "name": "Projeto POO – Professora Claudiany",
        "email": "exemplo@uninassau.edu.br"
    }
)


# ============================================================
#  🌐 CONFIGURAÇÃO DO CORS
# ============================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
#  📌 REGISTRO DE TODAS AS ROTAS
#    (agora organizadas por prefixo corretamente!)
# ============================================================
app.include_router(cliente_router, prefix="/api/clientes")
app.include_router(destino_router, prefix="/api/destinos")
app.include_router(reserva_router, prefix="/api/reservas")


# ============================================================
#  🏠 ROTA PRINCIPAL – HOME
# ============================================================
@app.get("/")
def home():
    return {
        "status": "online",
        "projeto": "API de Reservas de Viagens ✈️",
        "versao": "2.0.0",
        "endpoints": {
            "clientes": "/api/clientes",
            "destinos": "/api/destinos",
            "reservas": "/api/reservas",
        },
        "documentacao": {
            "swagger": "/docs",
            "redoc": "/redoc"
        },
        "mensagem": "🌍 Bem-vindo! Acesse /docs para testar a API."
    }




