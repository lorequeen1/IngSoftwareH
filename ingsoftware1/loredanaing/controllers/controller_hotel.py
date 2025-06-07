from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..services import HotelService
from ..serializers import HotelSerializer
from ..models import Hotel

class HotelViewSet(viewsets.ViewSet):
    def __init__(self, *args, **kwargs):
        self.service = HotelService()
        super().__init__(*args, **kwargs)

    def list(self, request):
        hoteles = self.service.get_all_hoteles()
        serializer = HotelSerializer(hoteles, many=True)
        return Response(serializer.data)

    def create(self, request):
        nombre = request.data.get('nombre')
        direccion = request.data.get('direccion')
        hotel = self.service.create_hotel(nombre, direccion)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        hotel = self.service.get_hotel_by_id(pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def update(self, request, pk=None):
        nombre = request.data.get('nombre')
        direccion = request.data.get('direccion')
        hotel = self.service.update_hotel(pk, nombre, direccion)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        self.service.delete_hotel(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
