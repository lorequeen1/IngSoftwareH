from ..repositories import HabitacionRepository

class HabitacionService:
    def __init__(self):
        self.repository = HabitacionRepository()

    def get_all_habitaciones(self):
        return self.repository.get_all()

    def get_habitacion_by_id(self, habitacion_id):
        return self.repository.get_by_id(habitacion_id)

    def create_habitacion(self, tipo, numero, estado):
        return self.repository.create(tipo, numero, estado)

    def update_habitacion(self, habitacion_id, tipo=None, numero=None, estado=None):
        return self.repository.update(habitacion_id, tipo, numero, estado)

    def delete_habitacion(self, habitacion_id):
        return self.repository.delete(habitacion_id)

    def reservar_habitacion(self, habitacion_id):
        habitacion = self.repository.get_by_id(habitacion_id)
        return habitacion.reservarhabitacion()

    def verificar_disponibilidad(self, habitacion_id):
        habitacion = self.repository.get_by_id(habitacion_id)
        return habitacion.verificardisponibilidad()