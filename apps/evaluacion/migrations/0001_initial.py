# Generated by Django 5.2.1 on 2025-05-28 06:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumnos', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criterio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('borrador', 'Borrador'), ('enviada', 'Enviada')], default='borrador', max_length=20)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.estudiante')),
            ],
            options={
                'unique_together': {('estudiante', 'curso')},
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('puntuacion', models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])),
                ('comentario', models.TextField(blank=True)),
                ('criterio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.criterio')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='evaluacion.evaluacion')),
            ],
        ),
    ]
