from ..repositories import HuespedRepository

class HuespedService:
    def __init__(self):
        self.repository = HuespedRepository()

    def get_all_huespedes(self):
        return self.repository.get_all()

    def get_huesped_by_id(self, huesped_id):
        return self.repository.get_by_id(huesped_id)

    def create_huesped(self, nombre, email):
        return self.repository.create(nombre, email)

    def update_huesped(self, huesped_id, nombre=None, email=None):
        return self.repository.update(huesped_id, nombre, email)

    def delete_huesped(self, huesped_id):
        return self.repository.delete(huesped_id)