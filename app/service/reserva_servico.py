from abc import ABC, abstractmethod
from app.dominio.reserva import Reserva
from app.dominio.reserva_nacional import ReservaNacional
from app.dominio.reserva_internacional import ReservaInternacional
from app.config.database import SessionLocal
from app.models.models import DBReserva, DBDestino, DBCliente


# ======================================================
#  INTERFACE (CONTRATO)
# ======================================================
class ServicoViagem(ABC):

    @abstractmethod
    def criar_reserva(self, dados: dict) -> dict:
        pass


# ======================================================
#  SERVICE RESPONSÁVEL PELA LÓGICA DE RESERVA
# ======================================================
class ReservaService:

    @staticmethod
    def criar_reserva(dados):
        db = SessionLocal()

        # 1️⃣ Buscar cliente
        cliente = db.query(DBCliente).filter(DBCliente.id == dados.cliente_id).first()
        if not cliente:
            return {"erro": "Cliente não encontrado"}

        # 2️⃣ Buscar destino
        destino = db.query(DBDestino).filter(DBDestino.id == dados.destino_id).first()
        if not destino:
            return {"erro": "Destino não encontrado"}

        # 3️⃣ Criar reserva POO
        if dados.tipo_reserva.lower() == "nacional":
            reserva_poo = ReservaNacional(
                id_cliente=dados.cliente_id,
                destino=destino.nome,
                data_viagem=dados.data_viagem,
                num_pessoas=dados.num_pessoas,
                tipo_reserva=dados.tipo_reserva,
            )
        else:
            reserva_poo = ReservaInternacional(
                id_cliente=dados.cliente_id,
                destino=destino.nome,
                data_viagem=dados.data_viagem,
                num_pessoas=dados.num_pessoas,
                tipo_reserva=dados.tipo_reserva,
            )

        # 4️⃣ Calcular preço final
        preco_final = reserva_poo.calcular_preco(destino.preco_base)

        # 5️⃣ Gravar no banco
        nova_reserva = DBReserva(
            cliente_id=dados.cliente_id,
            destino_id=dados.destino_id,
            data_viagem=dados.data_viagem,
            num_pessoas=dados.num_pessoas,
            tipo_reserva=dados.tipo_reserva,
            preco_final=preco_final
        )

        db.add(nova_reserva)
        db.commit()
        db.refresh(nova_reserva)

        return {
            "id": nova_reserva.id,
            "cliente": cliente.nome,
            "destino": destino.nome,
            "data_viagem": str(nova_reserva.data_viagem),
            "num_pessoas": nova_reserva.num_pessoas,
            "tipo_reserva": nova_reserva.tipo_reserva,
            "preco_final": nova_reserva.preco_final
        }

        
