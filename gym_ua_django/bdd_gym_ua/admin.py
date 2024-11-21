from django.contrib import admin
from .models import Docentes, Facultades, Modalidades, Sedes, Carreras, DetalleCarrera, Alumnos, Detalle_Asistencia


admin.site.register(Docentes)
admin.site.register(Facultades)
admin.site.register(Modalidades)
admin.site.register(Sedes)
admin.site.register(Carreras)
admin.site.register(DetalleCarrera)
admin.site.register(Alumnos)
admin.site.register(Detalle_Asistencia)
