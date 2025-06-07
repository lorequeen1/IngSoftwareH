from django.db import models
from django.shortcuts import get_object_or_404

class Pago(models.Model):
    METODO_CHOICES = [
        ('CREDITO', 'Crédito'),
        ('DEBITO', 'Débito'),
        ('EFECTIVO', 'Efectivo'),
    ]
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=10, choices=METODO_CHOICES)

    def procesarpago(self, monto, metodo):
        self.monto = monto
        self.metodo = metodo
        self.save()
        return self

    def reembolsarpago(self):
        # Aquí podrías agregar la lógica para procesar un reembolso, si es necesario.
        self.delete()
        return True

    def __str__(self):
        return f'Pago de {self.monto} por {self.metodo}'
