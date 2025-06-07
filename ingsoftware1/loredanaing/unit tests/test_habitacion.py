import pytest
from App_Hotel.models import Habitacion
from App_Hotel.services import HabitacionService
from App_Hotel.repositories import HabitacionRepository
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

