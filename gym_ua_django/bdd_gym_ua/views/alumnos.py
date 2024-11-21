from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Alumnos, Sedes, Modalidades, Facultades, Carreras, DetalleCarrera
from ..serializers import AlumnoSerializer


class ValidacionView(APIView):
    def get(self, request):
        return Response({'mensaje': 'funciona'})


class AlumnoListCreate(APIView):
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
                    'apellido_alumno': data.get('apellido_alumno'),
                    'correo_alumno': data.get('correo_alumno'),
                    'telefono_alumno': data.get('telefono_alumno'),
                    'fk_carrera_alumno': detalle_carrera.id_detalle_carrera
                }
                serializer = AlumnoSerializer(data=alumno_data)
                if serializer.is_valid():
                    serializer.save()

                    return Response({'mensaje': 'Alumno creado exitosamente', 'datos': serializer.data}, status=status.HTTP_201_CREATED)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'mensaje': 'No se pudo crear el alumno, verifique los datos'}, status=status.HTTP_400_BAD_REQUEST)


class ListaAlumnos(APIView):
    def get(self, request):
        lista_alumnos = Alumnos.objects.select_related(
            'fk_carrera_alumno__fk_sede_detalle'
        ).values(
            'rut_alumno',
            'nombre_alumno',
            'apellido_Paterno_Alumno',
            'apellido_Materno_Alumno',
            'correo_alumno',
            'telefono_alumno',
            'telefono_Emergencia_Alumno',
            'fk_carrera_alumno__fk_sede_detalle__nombre_sede'
        )

        result = [
            {
                'rut_alumno': alumno['rut_alumno'],
                'nombre_alumno': alumno['nombre_alumno'],
                'apellido_Paterno_Alumno': alumno['apellido_Paterno_Alumno'],
                'apellido_Materno_Alumno': alumno['apellido_Materno_Alumno'],
                'correo_alumno': alumno['correo_alumno'],
                'telefono_alumno': alumno['telefono_alumno'],
                'telefono_Emergencia_Alumno': alumno['telefono_Emergencia_Alumno'],
                'sede': alumno['fk_carrera_alumno__fk_sede_detalle__nombre_sede']
            }
            for alumno in lista_alumnos
        ]

        return Response(result, status=200)


class AlumnosView(APIView):
    def get(self, request):
        alumnos = Alumnos.objects.all()
        serializer = AlumnoSerializer(alumnos, many=True)
        return Response(serializer.data)
