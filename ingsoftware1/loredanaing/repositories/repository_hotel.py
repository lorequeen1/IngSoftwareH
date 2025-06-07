from ..models import Hotel

class HotelRepository:
    def get_all(self):
        """
        Obtiene todos los hoteles.
        """
        return Hotel.objects.all()

    def get_by_id(self, hotel_id):
        """
        Obtiene un hotel por su ID.
        """
        return Hotel.objects.get(pk=hotel_id)

    def create(self, nombre, direccion):
        """
        Crea un nuevo hotel.
        """
        return Hotel.objects.create(nombre=nombre, direccion=direccion)

    def update(self, hotel_id, nombre=None, direccion=None):
        """
        Actualiza un hotel existente.
        """
        hotel = Hotel.objects.get(pk=hotel_id)
        if nombre:
            hotel.nombre = nombre
        if direccion:
            hotel.direccion = direccion
        hotel.save()
        return hotel

    def delete(self, hotel_id):
        """
        Elimina un hotel por su ID.
        """
        hotel = Hotel.objects.get(pk=hotel_id)
        hotel.delete()