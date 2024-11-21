from django.contrib.auth import authenticate  # Importamos authenticate
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers import DocenteSerializer
from ..models import Docentes
from django.contrib.auth.hashers import check_password


class DocenteListCreate(views.APIView):
    def post(self, request):
        serializer = DocenteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request):
        correo = request.data.get('correo_docente')
        password = request.data.get('password')
        docente = Docentes.objects.filter(correo_docente=correo).first()

        if docente:
            if check_password(password, docente.password):
                refresh = RefreshToken.for_user(docente)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)

        return Response({'error': 'Credenciales incorrectas'}, status=status.HTTP_401_UNAUTHORIZED)
