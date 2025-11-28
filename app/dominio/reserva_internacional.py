from app.dominio.reserva import Reserva

class ReservaInternacional(Reserva):
    TAXA_INTERNACIONAL = 0.15

    def calcular_preco(self, preco_base_destino: float) -> float:
        preco_base = super().calcular_preco(preco_base_destino)
        return round(preco_base * (1 + self.TAXA_INTERNACIONAL), 2)

