import pytest
from App_Hotel.models import Pago
from App_Hotel.services import PagoService
from App_Hotel.repositories import PagoRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_pago_creation():
    pago = Pago.objects.create(monto=100.0, metodo="MONTO")
    assert float(pago.monto) == 100.0
    assert pago.metodo == "MONTO"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_pago_service():
    service = PagoService()
    pago = service.create_pago(150.0, "EFECTIVO")
    assert float(pago.monto) == 150.0
    assert pago.metodo == "EFECTIVO"

# Pruebas de Repositorios
@pytest.mark.django_db
def test_get_all_pagos_repository():
    repository = PagoRepository()
    pagos = repository.get_all()
    assert len(pagos) == 0  # Asumiendo que la base de datos esté vacía al inicio de la prueba

# Pruebas de Controladores (ViewSets)
@pytest.mark.django_db
def test_get_pagos_viewset():
    client = APIClient()
    response = client.get(reverse('pago-list'))
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_create_pago_viewset():
    client = APIClient()
    data = {'monto': 200.0, 'metodo': 'DEBITO'}
    response = client.post(reverse('pago-list'), data, format='json')
    assert response.status_code == 201
    assert float(response.json()['monto']) == 200.0
    assert response.json()['metodo'] == 'DEBITO'