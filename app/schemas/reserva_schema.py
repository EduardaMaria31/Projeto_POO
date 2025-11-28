from pydantic import BaseModel, field_validator
from datetime import date


# ======================================================
#  BASE
# ======================================================
class ReservaBase(BaseModel):
    cliente_id: int
    destino_id: int
    data_viagem: date
    num_pessoas: int
    tipo_reserva: str

    # Validações adicionais
    @field_validator("tipo_reserva")
    def validar_tipo_reserva(cls, v):
        tipos_validos = ["nacional", "internacional"]
        if v.lower() not in tipos_validos:
            raise ValueError("tipo_reserva deve ser 'nacional' ou 'internacional'")
        return v.lower()

    @field_validator("num_pessoas")
    def validar_numero_pessoas(cls, v):
        if v < 1:
            raise ValueError("num_pessoas deve ser pelo menos 1")
        return v



class ReservaCreate(ReservaBase):
    """Usado no POST. Igual ao Base."""



class ReservaOut(ReservaBase):
    id: int
    preco_final: float

    model_config = {
        "from_attributes": True  # Pydantic v2 (substitui orm_mode=True)
    }

