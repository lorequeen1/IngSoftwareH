from django.db import models
from django.shortcuts import get_object_or_404

class Personal(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)

    def agregar(self, nombre, puesto):
        personal = Personal(nombre=nombre, puesto=puesto)
        personal.save()
        return personal

    def actualizar(self, personal_id, nombre=None, puesto=None):
        personal = get_object_or_404(Personal, id=personal_id)
        if nombre:
            personal.nombre = nombre
        if puesto:
            personal.puesto = puesto
        personal.save()
        return personal

    def eliminar(self, personal_id):
        personal = get_object_or_404(Personal, id=personal_id)
        personal.delete()
        return True

    def __str__(self):
        return self.nombre
