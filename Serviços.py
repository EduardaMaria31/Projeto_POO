from abc import ABC, abstractmethod
from datetime import date
from typing import List, Dict

class ServicoViagem(ABC):
    @abstractmethod
    def cadastrar_destino(self, nome: str, preco: float, datas: str) -> None: pass

    @abstractmethod
    def criar_reserva(self, reserva_data: Dict) -> dict: pass

class Reserva:
    def __init__(self, id_cliente: str, destino: str, data_viagem: date, num_pessoas: int):
        self.id_cliente = id_cliente
        self.destino = destino
        self.data_viagem = data_viagem
        self.num_pessoas = num_pessoas
        self.preco_base = 0.0

    def calcular_preco(self, preco_base_destino: float) -> float:
        self.preco_base = preco_base_destino * self.num_pessoas
        return self.preco_base
    

class ReservaNacional(Reserva):
    TAXA_NACIONAL = 0.05

    def calcular_preco(self, preco_base_destino: float) -> float:
        preco_base = super().calcular_preco(preco_base_destino)
        preco_final = preco_base * (1 + self.TAXA_NACIONAL)
        return round(preco_final, 2)
    
class ReservaInternacional(Reserva):    
    FATOR_CAMBIO = 1.25
    TAXA_VIST0 = 100.0

    def calcular_preco(self, preco_base_destino: float) -> float:
        preco_base = super().calcular_preco(preco_base_destino)

        valor_ajustado = preco_base * self.FATOR_CAMBIO

        preco_final = valor_ajustado + (self.TAXA_VIST0 * self.num_pessoas)
        return round(preco_final, 2)
        
