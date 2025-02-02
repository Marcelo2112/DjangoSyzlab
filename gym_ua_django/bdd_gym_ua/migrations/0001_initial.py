# Generated by Django 5.0.3 on 2024-03-25 19:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id_carrera', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_carrera', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('rut_docente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_docente', models.CharField(max_length=100)),
                ('apellidos_docente', models.CharField(max_length=100)),
                ('correo_docente', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Facultades',
            fields=[
                ('id_facultad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_facultad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidades',
            fields=[
                ('id_modalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_modalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sedes',
            fields=[
                ('id_sede', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sede', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCarrera',
            fields=[
                ('id_detalle_carrera', models.AutoField(primary_key=True, serialize=False)),
                ('fk_carrera_detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.carreras')),
                ('fk_facultad_detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.facultades')),
                ('fk_modalidad_detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.modalidades')),
                ('fk_sede_detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.sedes')),
            ],
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('rut_alumno', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_alumno', models.CharField(max_length=100)),
                ('apellido_alumno', models.CharField(max_length=100)),
                ('correo_alumno', models.EmailField(max_length=254)),
                ('telefono_alumno', models.IntegerField()),
                ('fk_carrera_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.detallecarrera')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Asistencia',
            fields=[
                ('id_detalle_asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('fk_rut_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.alumnos')),
                ('fk_rut_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.docentes')),
            ],
        ),
        migrations.CreateModel(
            name='DocenteSedes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.docentes')),
                ('id_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd_gym_ua.sedes')),
            ],
            options={
                'unique_together': {('rut_docente', 'id_sede')},
            },
        ),
    ]
