from ..repositories import ReservaRepository

class ReservaService:
    def __init__(self):
        self.repository = ReservaRepository()

    def get_all_reservas(self):
        return self.repository.get_all()

    def get_reserva_by_id(self, reserva_id):
        return self.repository.get_by_id(reserva_id)

    def create_reserva(self, fecha_entrada, fecha_salida):
        return self.repository.create(fecha_entrada, fecha_salida)

    def update_reserva(self, reserva_id, fecha_entrada=None, fecha_salida=None):
        return self.repository.update(reserva_id, fecha_entrada, fecha_salida)

    def delete_reserva(self, reserva_id):
        return self.repository.delete(reserva_id)

    def cancelar_reserva(self, reserva_id):
        reserva = self.repository.get_by_id(reserva_id)
        return reserva.cancelarreserva()

    def modificar_reserva(self, reserva_id, fecha_entrada, fecha_salida):
        reserva = self.repository.get_by_id(reserva_id)
        return reserva.modificarreserva()