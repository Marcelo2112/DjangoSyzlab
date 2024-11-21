from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
import bcrypt


class DocenteManager(BaseUserManager):
    def create_user(self, correo_docente, password=None, **extra_fields):
        if not correo_docente:
            raise ValueError('El correo del docente es obligatorio')
        user = self.model(correo_docente=correo_docente, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_docente, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')

        return self.create_user(correo_docente, password, **extra_fields)

# Modelo de Docentes


class Docentes(AbstractBaseUser):
    rut_docente = models.AutoField(primary_key=True)
    nombre_docente = models.CharField(max_length=100, null=False)
    apellidos_docente = models.CharField(max_length=100, null=False)
    correo_docente = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=256, null=False)

    USERNAME_FIELD = 'correo_docente'
    REQUIRED_FIELDS = ['nombre_docente', 'apellidos_docente']

    objects = DocenteManager()

    def __str__(self):
        return self.correo_docente

# Modelo de Facultades


class Facultades(models.Model):
    id_facultad = models.AutoField(primary_key=True)
    nombre_facultad = models.CharField(max_length=50, null=False)

# Modelo de Modalidades


class Modalidades(models.Model):
    id_modalidad = models.AutoField(primary_key=True)
    nombre_modalidad = models.CharField(max_length=50, null=False)

# Modelo de Sedes


class Sedes(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=50, null=False)

# Modelo de Carreras


class Carreras(models.Model):
    id_carrera = models.AutoField(primary_key=True)
    nombre_carrera = models.CharField(max_length=50, null=False)

# Modelo de DetalleCarrera


class DetalleCarrera(models.Model):
    id_detalle_carrera = models.AutoField(primary_key=True)
    fk_sede_detalle = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    fk_facultad_detalle = models.ForeignKey(
        Facultades, on_delete=models.CASCADE)
    fk_modalidad_detalle = models.ForeignKey(
        Modalidades, on_delete=models.CASCADE)
    fk_carrera_detalle = models.ForeignKey(Carreras, on_delete=models.CASCADE)

# Modelo de DocenteSedes


class DocenteSedes(models.Model):
    rut_docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    id_sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rut_docente', 'id_sede')

# Modelo de Alumnos


class Alumnos(models.Model):
    rut_alumno = models.IntegerField(primary_key=True)
    nombre_alumno = models.CharField(max_length=100, null=False)
    apellido_alumno = models.CharField(max_length=100, null=False)
    correo_alumno = models.EmailField(null=False)
    telefono_alumno = models.IntegerField(null=False)
    fk_carrera_alumno = models.ForeignKey(
        DetalleCarrera, on_delete=models.CASCADE)

# Modelo de Detalle_Asistencia


class Detalle_Asistencia(models.Model):
    id_detalle_asistencia = models.AutoField(primary_key=True)
    fk_rut_alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    fk_rut_docente = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
