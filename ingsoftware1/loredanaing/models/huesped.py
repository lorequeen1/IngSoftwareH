from django.db import models
from django.shortcuts import get_object_or_404

class Huesped(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()

    def registrarhuesped(self, nombre, email):
        huesped = Huesped(nombre=nombre, email=email)
        huesped.save()
        return huesped

    def actualizarhuesped(self, huesped_id, nombre=None, email=None):
        huesped = get_object_or_404(Huesped, id=huesped_id)
        if nombre:
            huesped.nombre = nombre
        if email:
            huesped.email = email
        huesped.save()
        return huesped

    def __str__(self):
        return self.nombre
