from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..services import HuespedService
from ..serializers import HuespedSerializer
from ..models import Huesped

class HuespedViewSet(viewsets.ViewSet):
    def __init__(self, *args, **kwargs):
        self.service = HuespedService()
        super().__init__(*args, **kwargs)

    def list(self, request):
        huespedes = Huesped.objects.all()
        serializer = HuespedSerializer(huespedes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = HuespedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            huesped = Huesped.objects.get(pk=pk)
        except Huesped.DoesNotExist:
            return Response({'error': 'Huesped not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HuespedSerializer(huesped)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            huesped = Huesped.objects.get(pk=pk)
        except Huesped.DoesNotExist:
            return Response({'error': 'Huesped not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = HuespedSerializer(huesped, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            huesped = Huesped.objects.get(pk=pk)
        except Huesped.DoesNotExist:
            return Response({'error': 'Huesped not found'}, status=status.HTTP_404_NOT_FOUND)

        huesped.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)