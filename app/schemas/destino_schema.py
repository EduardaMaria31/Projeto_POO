from pydantic import BaseModel, Field, PositiveFloat
from typing import Optional


class DestinoBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=60, description="Nome do destino turístico")
    preco_base: PositiveFloat = Field(..., description="Preço base mínimo do destino")
    disponibilidade: str = Field(..., min_length=3, max_length=30, description="Status de disponibilidade")
    descricao: Optional[str] = Field(None, max_length=300, description="Descrição detalhada do destino")

    model_config = {
        "from_attributes": True,  # substitui orm_mode no Pydantic v2
    }


class DestinoCreate(DestinoBase):
    """Modelo usado ao cadastrar um novo destino."""
    pass


class DestinoOut(DestinoBase):
    """Modelo retornado ao consultar um destino."""
    id: int = Field(..., description="ID único do destino")

