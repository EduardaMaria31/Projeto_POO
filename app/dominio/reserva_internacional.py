from app.dominio.reserva import Reserva

class ReservaInternacional(Reserva):
    TAXA_INTERNACIONAL = 0.15  # 15% de taxa

    def calcular_preco(self, preco_base_destino: float) -> float:
        preco_base = super().calcular_preco(preco_base_destino)
        preco_final = preco_base * (1 + self.TAXA_INTERNACIONAL)
        return round(preco_final, 2)
