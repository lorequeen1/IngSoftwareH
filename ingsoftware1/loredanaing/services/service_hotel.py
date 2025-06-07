from ..repositories import HotelRepository

class HotelService:
    def __init__(self):
        self.repository = HotelRepository()

    def get_all_hoteles(self):
        return self.repository.get_all()

    def get_hotel_by_id(self, hotel_id):
        return self.repository.get_by_id(hotel_id)

    def create_hotel(self, nombre, direccion):
        return self.repository.create(nombre, direccion)

    def update_hotel(self, hotel_id, nombre=None, direccion=None):
        return self.repository.update(hotel_id, nombre, direccion)

    def delete_hotel(self, hotel_id):
        return self.repository.delete(hotel_id)