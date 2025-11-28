from datetime import date

class Reserva:
    """
    Classe base para qualquer tipo de reserva (nacional ou internacional).
    """
    def __init__(self, cliente_id: int, destino_id: int, data_viagem: date,
                 num_pessoas: int, tipo_reserva: str):
        self.cliente_id = cliente_id
        self.destino_id = destino_id
        self.data_viagem = data_viagem
        self.num_pessoas = num_pessoas
        self.tipo_reserva = tipo_reserva
        self.preco_base = 0.0

    def calcular_preco(self, preco_base_destino: float) -> float:
        """
        Cálculo básico:
        preço_base_destino × número de pessoas
        """
        self.preco_base = preco_base_destino * self.num_pessoas
        return self.preco_base

