from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..services import PagoService
from ..serializers import PagoSerializer
from ..models import Pago

class PagoViewSet(viewsets.ViewSet):
    def __init__(self, *args, **kwargs):
        self.service = PagoService()
        super().__init__(*args, **kwargs)

    def list(self, request):
        pagos = self.service.get_all_pagos()
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            pago = self.service.get_pago_by_id(pk)
        except Pago.DoesNotExist:
            return Response({'error': 'Pago not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PagoSerializer(pago)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            pago = self.service.get_pago_by_id(pk)
        except Pago.DoesNotExist:
            return Response({'error': 'Pago not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PagoSerializer(pago, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            pago = self.service.get_pago_by_id(pk)
        except Pago.DoesNotExist:
            return Response({'error': 'Pago not found'}, status=status.HTTP_404_NOT_FOUND)

        self.service.delete_pago(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
