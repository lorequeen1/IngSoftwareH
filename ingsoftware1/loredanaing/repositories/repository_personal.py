from ..models import Personal

class PersonalRepository:
    def get_all(self):
        """
        Obtiene todos los registros de personal.
        """
        return Personal.objects.all()

    def get_by_id(self, personal_id):
        """
        Obtiene un registro de personal por su ID.
        """
        return Personal.objects.get(pk=personal_id)

    def create(self, nombre, puesto):
        """
        Crea un nuevo registro de personal.
        """
        return Personal.objects.create(nombre=nombre, puesto=puesto)

    def update(self, personal_id, nombre=None, puesto=None):
        """
        Actualiza un registro de personal existente.
        """
        personal = Personal.objects.get(pk=personal_id)
        if nombre is not None:
            personal.nombre = nombre
        if puesto is not None:
            personal.puesto = puesto
        personal.save()
        return personal

    def delete(self, personal_id):
        """
        Elimina un registro de personal por su ID.
        """
        personal = Personal.objects.get(pk=personal_id)
        personal.delete()