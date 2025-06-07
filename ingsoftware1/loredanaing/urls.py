from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .controllers import *

router = DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet, basename='habitacion')
router.register(r'reservas', ReservaViewSet, basename='reserva')
router.register(r'hoteles', HotelViewSet, basename='hotel')
router.register(r'huespedes', HuespedViewSet, basename='huesped')
router.register(r'pago', PagoViewSet, basename='pago')
router.register(r'personal', PersonalViewSet, basename='personal')

urlpatterns = [

    path('', include(router.urls)),

]
