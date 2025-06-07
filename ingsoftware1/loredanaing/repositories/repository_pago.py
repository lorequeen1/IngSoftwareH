from ..models import Pago

class PagoRepository:
    def get_all(self):
        """
        Obtiene todos los pagos.
        """
        return Pago.objects.all()

    def get_by_id(self, pago_id):
        """
        Obtiene un pago por su ID.
        """
        return Pago.objects.get(pk=pago_id)

    def create(self, monto, metodo):
        """
        Crea un nuevo pago.
        """
        return Pago.objects.create(monto=monto, metodo=metodo)

    def update(self, pago_id, monto=None, metodo=None):
        """
        Actualiza un pago existente.
        """
        pago = Pago.objects.get(pk=pago_id)
        if monto is not None:
            pago.monto = monto
        if metodo is not None:
            pago.metodo = metodo
        pago.save()
        return pago

    def delete(self, pago_id):
        """
        Elimina un pago por su ID.
        """
        pago = Pago.objects.get(pk=pago_id)
        pago.reembolsarpago()
        return True