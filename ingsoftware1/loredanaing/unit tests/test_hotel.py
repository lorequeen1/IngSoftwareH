import pytest
from App_Hotel.models import Hotel
from App_Hotel.services import HotelService
from App_Hotel.repositories import HotelRepository
from rest_framework.test import APIClient
from django.urls import reverse

# Pruebas de Modelos
@pytest.mark.django_db
def test_hotel_creation():
    hotel = Hotel.objects.create(nombre="Hotel Test", direccion="Dirección Test")
    assert hotel.nombre == "Hotel Test"
    assert hotel.direccion == "Dirección Test"

# Pruebas de Servicios
@pytest.mark.django_db
def test_create_hotel_service():
    service = HotelService()
    hotel = service.create_hotel("Hotel Service Test", "Dirección Service Test")
    assert hotel.nombre == "Hotel Service Test"
    assert hotel.direccion == "Dirección Service Test"

