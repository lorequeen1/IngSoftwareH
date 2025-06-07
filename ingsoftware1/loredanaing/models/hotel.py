from django.db import models
from django.shortcuts import get_object_or_404

class Hotel(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()

    def agregarhotel(self, nombre, direccion):
        hotel = Hotel(nombre=nombre, direccion=direccion)
        hotel.save()
        return hotel

    def actualizarhotel(self, hotel_id, nombre=None, direccion=None):
        hotel = get_object_or_404(Hotel, id=hotel_id)
        if nombre:
            hotel.nombre = nombre
        if direccion:
            hotel.direccion = direccion
        hotel.save()
        return hotel

    def eliminarhotel(self, hotel_id):
        hotel = get_object_or_404(Hotel, id=hotel_id)
        hotel.delete()
        return True

    def __str__(self):
        return self.nombre
