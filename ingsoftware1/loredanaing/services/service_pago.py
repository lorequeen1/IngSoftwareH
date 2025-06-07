from ..repositories import PagoRepository

class PagoService:
    def __init__(self):
        self.repository = PagoRepository()

    def get_all_pagos(self):
        return self.repository.get_all()

    def get_pago_by_id(self, pago_id):
        return self.repository.get_by_id(pago_id)

    def create_pago(self, monto, metodo):
        return self.repository.create(monto, metodo)

    def update_pago(self, pago_id, monto=None, metodo=None):
        return self.repository.update(pago_id, monto, metodo)

    def delete_pago(self, pago_id):
        return self.repository.delete(pago_id)