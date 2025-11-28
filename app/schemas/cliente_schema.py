from pydantic import BaseModel


# ============================================================
# 🔹 BASE — Campos que o cliente sempre terá
# ============================================================
class ClienteBase(BaseModel):
    nome: str
    email: str
    telefone: str


# ============================================================
# 🔹 Para criar novos clientes (entrada da API)
# ============================================================
class ClienteCreate(ClienteBase):
    pass


# ============================================================
# 🔹 Para retornar dados para o usuário (saída da API)
# ============================================================
class ClienteOut(ClienteBase):
    id: int

    class Config:
        orm_mode = True



