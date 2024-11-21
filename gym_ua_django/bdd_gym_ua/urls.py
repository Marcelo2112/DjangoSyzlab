from django.urls import path
from .views import AlumnoListCreate, ValidacionView, AlumnosView
from .views import DatosAcademicos, SedeListCreate
from .views import AsistenciaListCreate, VerAsistenciaCompleta
from .views import DocenteListCreate, LoginView


urlpatterns = [
    # tus otras rutas...
    path('crear_alumno/', AlumnoListCreate.as_view(), name='crear-alumno'),
    path('lista_alumnos/', AlumnosView.as_view(), name='alumnos-view'),
    path('validacion/', ValidacionView.as_view(), name='validacion-view'),
    path('datos_academicos/', DatosAcademicos.as_view(), name='datos-academicos'),
    path('crear_sede/', SedeListCreate.as_view(), name='crear-sede'),
    path('ingresar_asistencia/', AsistenciaListCreate.as_view(),
         name='ingresar-asistencia'),
    path('asistencia/', VerAsistenciaCompleta.as_view(), name='asistencia'),
    path('crear_docente/', DocenteListCreate.as_view(), name='crear-docente'),
    path('login_docente/', LoginView.as_view(), name='login/docente')
]
