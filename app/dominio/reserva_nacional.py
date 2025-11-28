from app.dominio.reserva import Reserva

class ReservaNacional(Reserva):
    TAXA_NACIONAL = 0.05  # 5% de taxa

    def calcular_preco(self, preco_base_destino: float) -> float:
        preco_base = super().calcular_preco(preco_base_destino)
        preco_final = preco_base * (1 + self.TAXA_NACIONAL)
        return round(preco_final, 2)
