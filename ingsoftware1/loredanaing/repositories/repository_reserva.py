from ..models import Reserva

class ReservaRepository:
    def get_all(self):
        return Reserva.objects.all()

    def get_by_id(self, reserva_id):
        return Reserva.objects.get(pk=reserva_id)

    def create(self, fecha_entrada, fecha_salida):
        return Reserva.objects.create(fecha_entrada=fecha_entrada, fecha_salida=fecha_salida)

    def update(self, reserva_id, fecha_entrada=None, fecha_salida=None):
        reserva = Reserva.objects.get(pk=reserva_id)
        if fecha_entrada:
            reserva.fecha_entrada = fecha_entrada
        if fecha_salida:
            reserva.fecha_salida = fecha_salida
        reserva.save()
        return reserva

    def delete(self, reserva_id):
        reserva = Reserva.objects.get(pk=reserva_id)
        reserva.delete()