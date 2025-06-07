import pytest
from loredanaing.models import Habitacion
from loredanaing.services import HabitacionService
from loredanaing.repositories import HabitacionRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_habitacion_creation():
    habitacion = Habitacion.objects.create(tipo="SIMPLE", numero=9, estado="DISPONIBLE")
    assert habitacion.tipo == "SIMPLE"
    assert habitacion.numero == 9
    assert habitacion.estado == "DISPONIBLE"

@pytest.mark.django_db
def test_habitacion_creation():
    habitacion = Habitacion.objects.create(tipo="DOBLE", numero=9, estado="OCUPADA")
    assert habitacion.tipo == "DOBLE"
    assert habitacion.numero == 9
    assert habitacion.estado == "OCUPADA"

@pytest.mark.django_db
def test_habitacion_creation():
    habitacion = Habitacion.objects.create(tipo="SUIT", numero=9, estado="RESERVADA")
    assert habitacion.tipo == "SUIT"
    assert habitacion.numero == 9
    assert habitacion.estado == "RESERVADA"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_habitacion_service():
    service = HabitacionService()
    habitacion = service.create_habitacion("DOBLE", 20, "OCUPADA")
    assert habitacion.tipo == "DOBLE"
    assert habitacion.numero == 20
    assert habitacion.estado == "OCUPADA"

# Pruebas de Repositorios
@pytest.mark.django_db
def test_get_all_habitaciones_repository():
    repository = HabitacionRepository()
    habitaciones = repository.get_all()
    assert len(habitaciones) == 0  # Asumiendo que la base de datos esté vacía al inicio de la prueba

# Pruebas de Controladores (ViewSets)
@pytest.mark.django_db
def test_get_habitaciones_viewset():
    client = APIClient()
    response = client.get(reverse('habitacion-list'))
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_create_habitacion_viewset():
    client = APIClient()
    data = {'tipo': 'SUITE', 'numero': 1, 'estado': 'RESERVADA'}
    response = client.post(reverse('habitacion-list'), data, format='json')
    assert response.status_code == 201
    assert response.json()['tipo'] == 'SUITE'
    assert response.json()['numero'] == 1
    assert response.json()['estado'] == 'RESERVADA'