from fastapi import FastAPI
from .DataBase import Base, engine
from . import Models
from .Router import router 

Base.metdata.create_all(bind=engine)


app = FastAPI(
    title="API de Reservas de Viagens (Projeto POO)",
    description="POO- Professora Claudiany"
)

# Endpoint(Root)
@app.get("/")
def read_root():
    return {"Hello": "World"}
