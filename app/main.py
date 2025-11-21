from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import Base, engine
from app.rotas.routers import router

# ============================================================
#  🔧 CONFIGURAÇÃO DO BANCO – cria tabelas automaticamente
# ============================================================
Base.metadata.create_all(bind=engine)


# ============================================================
#  🚀 INICIALIZAÇÃO DA APLICAÇÃO FASTAPI
# ============================================================
app = FastAPI(
    title="API de Reservas de Viagens ✈️",
    description=(
        "Bem-vindo à **API de Reservas de Viagens**, um sistema desenvolvido para "
        "demonstrar conceitos de **Programação Orientada a Objetos (POO)**, "
        "**CRUD**, **camadas de serviço**, **modelos ORM** e boas práticas "
        "na construção de APIs modernas com *FastAPI*.\n\n"
        "➡️ Aqui você pode cadastrar clientes, destinos e criar reservas nacionais "
        "ou internacionais com cálculo de preço automático!"
    ),
    version="2.0.0",
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
    allow_origins=["*"],       # libera acesso ao front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
#  📌 REGISTRO DAS ROTAS DA APLICAÇÃO
# ============================================================
app.include_router(router)


# ============================================================
#  🏠 ROTA PRINCIPAL – APRESENTAÇÃO
# ============================================================
@app.get("/")
def read_root():
    return {
        "status": "online",
        "projeto": "API de Reservas de Viagens ✈️",
        "versao": "2.0.0",
        "descricao": "Sistema criado com FastAPI + SQLAlchemy + POO para fins educacionais.",
        "informacoes": {
            "endpoints_principais": {
                "/api/clientes": "Gerenciamento de clientes",
                "/api/destinos": "Cadastro de destinos",
                "/api/reservas": "Criação e listagem de reservas"
            },
            "documentacao_swagger": "/docs",
            "documentacao_redoc": "/redoc"
        },
        "mensagem": "🌍 Bem-vindo! Use /docs para testar a API de forma interativa."
    }


# Debug opcional (pode remover)
print("Rotas carregadas:", router.routes)

