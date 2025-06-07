from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..services import ReservaService
from ..serializers import ReservaSerializer
from ..models import Reserva

class ReservaViewSet(viewsets.ViewSet):
    def __init__(self, *args, **kwargs):
        self.service = ReservaService()
        super().__init__(*args, **kwargs)

    def list(self, request):
        reservas = self.service.get_all_reservas()
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            fecha_entrada = serializer.validated_data.get('fecha_entrada')
            fecha_salida = serializer.validated_data.get('fecha_salida')
            reserva = self.service.create_reserva(fecha_entrada, fecha_salida)
            serializer = ReservaSerializer(reserva)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            reserva = self.service.get_reserva_by_id(pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservaSerializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            reserva = self.service.get_reserva_by_id(pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            fecha_entrada = serializer.validated_data.get('fecha_entrada')
            fecha_salida = serializer.validated_data.get('fecha_salida')
            reserva = self.service.update_reserva(pk, fecha_entrada, fecha_salida)
            serializer = ReservaSerializer(reserva)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            reserva = self.service.get_reserva_by_id(pk)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)

        self.service.delete_reserva(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        try:
            result = self.service.cancelar_reserva(pk)
            return Response({"result": result}, status=status.HTTP_200_OK)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def modificar(self, request, pk=None):
        try:
            fecha_entrada = request.data.get('fecha_entrada')
            fecha_salida = request.data.get('fecha_salida')
            result = self.service.modificar_reserva(pk, fecha_entrada, fecha_salida)
            return Response({"result": result}, status=status.HTTP_200_OK)
        except Reserva.DoesNotExist:
            return Response({'error': 'Reserva not found'}, status=status.HTTP_404_NOT_FOUND)