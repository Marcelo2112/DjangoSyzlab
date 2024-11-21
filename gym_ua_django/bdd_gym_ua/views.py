from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Alumnos, Sedes, Modalidades, Facultades, Carreras, DetalleCarrera
from .serializers import AlumnoSerializer


class CrearAlumno(APIView):
    def post(self, request):
        data = request.data

        nombre_carrera = data.get('nombre_carrera')
        nombre_sede = data.get('nombre_sede')
        nombre_facultad = data.get('nombre_facultad')
        nombre_modalidad = data.get('nombre_modalidad')

        # Buscar IDs correspondientes a los valores proporcionados
        sede = Sedes.objects.filter(nombre_sede=nombre_sede).first()
        modalidad = Modalidades.objects.filter(
            nombre_modalidad=nombre_modalidad).first()
        facultad = Facultades.objects.filter(
            nombre_facultad=nombre_facultad).first()
        carrera = Carreras.objects.filter(
            nombre_carrera=nombre_carrera).first()

        if sede and modalidad and facultad and carrera:
            detalle_carrera = DetalleCarrera.objects.filter(
                fk_sede_detalle=sede,
                fk_modalidad_detalle=modalidad,
                fk_facultad_detalle=facultad,
                fk_carrera_detalle=carrera
            ).first()

            if detalle_carrera:
                alumno_data = {
                    'rut_alumno': data.get('rut_alumno'),
                    'nombre_alumno': data.get('nombre_alumno'),
                    'correo_alumno': data.get('correo_alumno'),
                    'telefono_alumno': data.get('telefono_alumno'),
                    'fk_carrera_alumno': detalle_carrera.id_detalle_carrera
                }
                serializer = AlumnoSerializer(data=alumno_data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'mensaje': 'Alumno creado exitosamente'}, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_BAD_REQUEST)

        return Response({'mensaje': 'No se pudo crear el alumno, verifique los datos'}, status=status.HTTP_400_BAD_REQUEST)
