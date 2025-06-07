from ..models import Huesped

class HuespedRepository:
    def get_all(self):
        """
        Obtiene todos los huéspedes.
        """
        return Huesped.objects.all()

    def get_by_id(self, huesped_id):
        """
        Obtiene un huésped por su ID.
        """
        return Huesped.objects.get(pk=huesped_id)

    def create(self, nombre, email):
        """
        Crea un nuevo huésped.
        """
        return Huesped.objects.create(nombre=nombre, email=email)

    def update(self, huesped_id, nombre=None, email=None):
        """
        Actualiza un huésped existente.
        """
        huesped = Huesped.objects.get(pk=huesped_id)
        if nombre:
            huesped.nombre = nombre
        if email:
            huesped.email = email
        huesped.save()
        return huesped

    def delete(self, huesped_id):
        """
        Elimina un huésped por su ID.
        """
        huesped = Huesped.objects.get(pk=huesped_id)
        huesped.delete()