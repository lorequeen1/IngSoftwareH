from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..services import PersonalService
from ..serializers import PersonalSerializer
from ..models import Personal

class PersonalViewSet(viewsets.ViewSet):
    def __init__(self, *args, **kwargs):
        self.service = PersonalService()
        super().__init__(*args, **kwargs)

    def list(self, request):
        personal = self.service.get_all_personal()
        serializer = PersonalSerializer(personal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PersonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            personal = self.service.get_personal_by_id(pk)
        except Personal.DoesNotExist:
            return Response({'error': 'Personal not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonalSerializer(personal)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            personal = self.service.get_personal_by_id(pk)
        except Personal.DoesNotExist:
            return Response({'error': 'Personal not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonalSerializer(personal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            personal = self.service.get_personal_by_id(pk)
        except Personal.DoesNotExist:
            return Response({'error': 'Personal not found'}, status=status.HTTP_404_NOT_FOUND)

        self.service.delete_personal(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
