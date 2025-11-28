from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.dominio.reserva_nacional import ReservaNacional
from app.dominio.reserva_internacional import ReservaInternacional
from app.models.models import DBReserva, DBDestino, DBCliente
from app.schemas.reserva_schema import ReservaCreate


# ======================================================
#  INTERFACE / CONTRATO
# ======================================================
class ServicoViagem(ABC):

    @abstractmethod
    def criar_reserva(self, dados: dict) -> dict:
        pass


# ======================================================
#  SERVICE RESPONSÁVEL PELA LÓGICA DE RESERVAS
# ======================================================
class ReservaService:

    def __init__(self, db: Session):
        self.db = db     # Banco disponível para todos os métodos POO

    def criar_reserva(self, dados: ReservaCreate):

        # Buscar cliente
        cliente = self.db.query(DBCliente).filter(DBCliente.id == dados.cliente_id).first()
        if not cliente:
            return {"erro": "Cliente não encontrado"}

        # Buscar destino
        destino = self.db.query(DBDestino).filter(DBDestino.id == dados.destino_id).first()
        if not destino:
            return {"erro": "Destino não encontrado"}

        # Criar OBJETO POO usando polimorfismo
        if dados.tipo_reserva.lower() == "nacional":
            reserva_poo = ReservaNacional(
                cliente_id=dados.cliente_id,
                destino_id=dados.destino_id,
                data_viagem=dados.data_viagem,
                num_pessoas=dados.num_pessoas,
                tipo_reserva=dados.tipo_reserva,
            )

        else:
            reserva_poo = ReservaInternacional(
                cliente_id=dados.cliente_id,
                destino_id=dados.destino_id,
                data_viagem=dados.data_viagem,
                num_pessoas=dados.num_pessoas,
                tipo_reserva=dados.tipo_reserva,
            )

        # Calcular preço final usando o método polimórfico
        preco_final = reserva_poo.calcular_preco(destino.preco_base)

        # Criar ORM para salvar no banco
        nova_reserva = DBReserva(
            cliente_id=dados.cliente_id,
            destino_id=dados.destino_id,
            data_viagem=dados.data_viagem,
            num_pessoas=dados.num_pessoas,
            tipo_reserva=dados.tipo_reserva,
            preco_final=preco_final
        )

        self.db.add(nova_reserva)
        self.db.commit()
        self.db.refresh(nova_reserva)

        return nova_reserva


        
