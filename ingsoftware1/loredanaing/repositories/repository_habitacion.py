from ..models import Habitacion

class HabitacionRepository:
    def get_all(self):
        return Habitacion.objects.all()

    def get_by_id(self, habitacion_id):
        return Habitacion.objects.get(pk=habitacion_id)

    def create(self, tipo, numero, estado):
        return Habitacion.objects.create(tipo=tipo, numero=numero, estado=estado)

    def update(self, habitacion_id, tipo=None, numero=None, estado=None):
        habitacion = Habitacion.objects.get(pk=habitacion_id)
        if tipo:
            habitacion.tipo = tipo
        if numero:
            habitacion.numero = numero
        if estado:
            habitacion.estado = estado
        habitacion.save()
        return habitacion

    def delete(self, habitacion_id):
        habitacion = Habitacion.objects.get(pk=habitacion_id)
        habitacion.delete()