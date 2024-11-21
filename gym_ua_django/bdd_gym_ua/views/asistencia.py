from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Detalle_Asistencia
from django.utils.timezone import make_aware
from datetime import datetime, timedelta


class AsistenciaListCreate(APIView):
    def post(self, request):
        datos = request.data
        rut_alumno = datos.get('rut_alumno')
        fecha_actual = datetime.now().date()

        docente_id = datos.get('docente_id')

        if not rut_alumno:
            return Response({'Mensaje': 'Se requiere rut del alumno'}, status=status.HTTP_400_BAD_REQUEST)

        alumno = Alumnos.objects.filter(rut_alumno=rut_alumno).first()

        if not alumno:
            return Response({'Mensaje': 'Alumno no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        fecha_inicio_dia = make_aware(
            datetime.combine(fecha_actual, datetime.min.time()))
        fecha_fin_dia = fecha_inicio_dia + timedelta(days=1)

        asistencia_existe = Detalle_Asistencia.objects.filter(
            fk_rut_alumno=alumno.rut_alumno,
            date_time__range=(fecha_inicio_dia, fecha_fin_dia)
        ).first()

        if asistencia_existe:
            return Response({'Mensaje': 'Ya existe asistencia '}, status=status.HTTP_409_CONFLICT)

        nueva_asistencia = Detalle_Asistencia(
            fk_rut_alumno=alumno,
            fk_rut_docente_id=docente_id,
            date_time=datetime.now()
        )
        nueva_asistencia.save()

        serializer = DetalleAsistenciaSerializer(nueva_asistencia)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerAsistencia(APIView):
    def get(self, request):
        docente = request.user
        asistencias = Detalle_Asistencia.objects.filter(
            fk_rut_docente=docente.id)
        serializer = DetalleAsistenciaSerializer(asistencias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AsistenciaAlumnos(APIView):
    def get(self, request):
        zona_horaria = timezone('America/Santiago')
        ahora_chile = make_aware(datetime.now(), timezone=zona_horaria)
        inicio_dia = ahora_chile.replace(
            hour=0, minute=0, second=0, microsecond=0)
        fin_dia = inicio_dia + timedelta(days=1)

        resultados = Detalle_Asistencia.objects.filter(
            date_time__gte=inicio_dia,
            date_time__lt=fin_dia
        ).select_related('fk_rut_alumno', 'fk_rut_alumno__fk_carrera_alumno')

        asistencias = []
        for asistencia in resultados:
            alumno = asistencia.fk_rut_alumno
            carrera = alumno.fk_carrera_alumno.fk_carrera_detalle
            hora_local = asistencia.date_time.astimezone(zona_horaria)

            asistencias.append({
                "rut_alumno": alumno.rut_alumno,
                "nombre": alumno.nombre_alumno,
                "apellido_paterno": alumno.apellido_Paterno_Alumno,
                "apellido_materno": alumno.apellido_Materno_Alumno,
                "carrera": carrera.nombre_carrera,
                "hora": hora_local.strftime("%H:%M")
            })

        return Response(asistencias, status=status.HTTP_200_OK)
