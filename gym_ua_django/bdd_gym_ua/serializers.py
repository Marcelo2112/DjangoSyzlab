from rest_framework import serializers
from .models import Alumnos, Docentes, Facultades, Modalidades, Sedes, Carreras, DetalleCarrera, Detalle_Asistencia


class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ['rut_alumno', 'nombre_alumno', 'apellido_alumno',
                  'correo_alumno', 'telefono_alumno', 'fk_carrera_alumno']


class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docentes
        fields = ['rut_docente', 'nombre_docente',
                  'apellidos_docente', 'correo_docente', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        docente = Docentes.objects.create_user(**validated_data)
        return docente


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultades
        fields = '__all__'


class ModalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidades
        fields = '__all__'  # si no necesitos todos los campos aca defino cuales si


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = '__all__'


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = ['nombre_carrera']


class DetalleAsistenciaSerializer(serializers.ModelSerializer):
    alumno = AlumnoSerializer(source='fk_rut_alumno', read_only=True)

    class Meta:
        model = Detalle_Asistencia
        fields = ['alumno', 'date_time']
