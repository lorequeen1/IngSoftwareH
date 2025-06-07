# app_Hotel/models/habitacion.py

from django.db import models
from django.shortcuts import get_object_or_404

class Habitacion(models.Model):
    TIPO_CHOICES = [
        ('SIMPLE', 'Simple'),
        ('DOBLE', 'Doble'),
        ('SUITE', 'Suite'),
    ]
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('OCUPADA', 'Ocupada'),
        ('RESERVADA', 'Reservada'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    numero = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)

    def reservarhabitacion(self):
        if self.estado == 'DISPONIBLE':
            self.estado = 'RESERVADA'
            self.save()
            return True
        return False

    def verificardisponibilidad(self):
        return self.estado == 'DISPONIBLE'

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo}'