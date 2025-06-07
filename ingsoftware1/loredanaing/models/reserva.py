from django.db import models
from django.shortcuts import get_object_or_404
from datetime import datetime

class Reserva(models.Model):
    fecha_entrada = models.CharField(max_length=10)
    fecha_salida = models.CharField(max_length=10) 

    def crearreserva(self, fecha_entrada, fecha_salida):
        reserva = Reserva(fecha_entrada=fecha_entrada, fecha_salida=fecha_salida)
        reserva.save()
        return reserva

    def cancelarreserva(self):
        self.delete()
        return True

    def modificarreserva(self, fecha_entrada=None, fecha_salida=None):
        if fecha_entrada:
            self.fecha_entrada = fecha_entrada
        if fecha_salida:
            self.fecha_salida = fecha_salida
        self.save()
        return self

    def __str__(self):
        return f'Reserva desde {self.fecha_entrada} hasta {self.fecha_salida}'