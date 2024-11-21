from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Sedes, Modalidades, Facultades, Carreras
from ..serializers import SedeSerializer, ModalidadSerializer, FacultadSerializer, CarreraSerializer


class DatosAcademicos(APIView):
    def get(self, request):
        return Response({'mensaje': 'Estamos en datos academicos'})


class SedeListCreate(APIView):
    def post(self, request):
        serializer = SedeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
