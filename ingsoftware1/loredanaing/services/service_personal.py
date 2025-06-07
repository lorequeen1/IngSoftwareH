from ..repositories import PersonalRepository

class PersonalService:
    def __init__(self):
        self.repository = PersonalRepository()

    def get_all_personal(self):
        return self.repository.get_all()

    def get_personal_by_id(self, personal_id):
        return self.repository.get_by_id(personal_id)

    def create_personal(self, nombre, puesto):
        return self.repository.create(nombre, puesto)

    def update_personal(self, personal_id, nombre=None, puesto=None):
        return self.repository.update(personal_id, nombre, puesto)

    def delete_personal(self, personal_id):
        return self.repository.delete(personal_id)