import pytest
from App_Hotel.models import Huesped
from App_Hotel.services import HuespedService
from App_Hotel.repositories import HuespedRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_huesped_creation():
    huesped = Huesped.objects.create(nombre="Pedro", email="correo@prueba.com")
    assert huesped.nombre == "Pedro"
    assert huesped.email == "correo@prueba.com"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_huesped_service():
    service = HuespedService()
    huesped = service.create_huesped("Pablo", "prueba@correo.com")
    assert huesped.nombre == "Pablo"
    assert huesped.email == "prueba@correo.com"
    
# Pruebas de Repositorios
@pytest.mark.django_db
def test_get_all_huespedes_repository():
    repository = HuespedRepository()
    huespedes = repository.get_all()
    assert len(huespedes) == 0  # Asumiendo que la base de datos esté vacía al inicio de la prueba

# Pruebas de Controladores (ViewSets)
@pytest.mark.django_db
def test_get_huespedes_viewset():
    client = APIClient()
    response = client.get(reverse('huesped-list'))
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.django_db
def test_create_huesped_viewset():
    client = APIClient()
    data = {'nombre': 'Sergio', "email": 'correodeprueba@gmail.com'}
    response = client.post(reverse('huesped-list'), data)
    assert response.status_code == 201
    assert response.json()['nombre'] == 'Sergio'
    assert response.json()['email'] == 'correodeprueba@gmail.com'