import pytest
from App_Hotel.models import Reserva
from App_Hotel.services import ReservaService
from App_Hotel.repositories import ReservaRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_reserva_creation():
    reserva = Reserva.objects.create(fecha_entrada="2024-08-01", fecha_salida="2024-08-05")
    assert reserva.fecha_entrada == "2024-08-01"
    assert reserva.fecha_salida == "2024-08-05"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_reserva_service():
    service = ReservaService()
    reserva = service.create_reserva("2024-08-10", "2024-08-15")
    assert reserva.fecha_entrada == "2024-08-10"
    assert reserva.fecha_salida == "2024-08-15"

# Pruebas de Repositorios
@pytest.mark.django_db
def test_get_all_reservas_repository():
    repository = ReservaRepository()
    reservas = repository.get_all()
    assert len(reservas) == 0  # Asumiendo que la base de datos esté vacía al inicio de la prueba

# Pruebas de Controladores (ViewSets)
@pytest.mark.django_db
def test_get_reservas_viewset():
    client = APIClient()
    response = client.get(reverse('reserva-list'))
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_create_reserva_viewset():
    client = APIClient()
    data = {'fecha_entrada': '2024-08-20', 'fecha_salida': '2024-08-25'}
    response = client.post(reverse('reserva-list'), data)
    assert response.status_code == 201
    assert response.json()['fecha_entrada'] == '2024-08-20'
    assert response.json()['fecha_salida'] == '2024-08-25'