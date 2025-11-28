from datetime import date

class Reserva:
    def __init__(self, cliente_id: int, destino_id: int, data_viagem: date,
                 num_pessoas: int, tipo_reserva: str):
        self.cliente_id = cliente_id
        self.destino_id = destino_id
        self.data_viagem = data_viagem
        self.num_pessoas = num_pessoas
        self.tipo = tipo_reserva
        self.preco_base = 0.0

    # cálculo básico = preço_base_destino x num_pessoas
    def calcular_preco(self, preco_base_destino: float) -> float:
        self.preco_base = preco_base_destino * self.num_pessoas
        return self.preco_base
