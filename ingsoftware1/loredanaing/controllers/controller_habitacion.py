from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..serializers import HabitacionSerializer
from ..services import HabitacionService
from ..models import Habitacion

class HabitacionViewSet(viewsets.ViewSet):
    def list(self, request):
        habitacion_list = Habitacion.objects.all()
        serializer = HabitacionSerializer(habitacion_list, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            habitacion = Habitacion.objects.get(pk=pk)
            serializer = HabitacionSerializer(habitacion)
            return Response(serializer.data)
        except Habitacion.DoesNotExist:
            return Response({'error': 'Habitacion not found'}, status=404)

    def create(self, request):
        serializer = HabitacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post'])
    def reservar(self, request, pk=None):
        service = HabitacionService()
        result = service.reservar_habitacion(pk)
        return Response({"result": result})

    @action(detail=True, methods=['post'])
    def disponibilidad(self, request, pk=None):
        service = HabitacionService()
        result = service.verificar_disponibilidad(pk)
        return Response({"disponible": result})