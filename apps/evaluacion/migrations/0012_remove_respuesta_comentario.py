# Generated by Django 5.0.6 on 2025-06-04 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0011_evaluacion_comentario_general'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='comentario',
        ),
    ]
