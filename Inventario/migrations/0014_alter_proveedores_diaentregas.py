# Generated by Django 4.1.7 on 2023-06-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0013_alter_artlimpieza_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='DiaEntregas',
            field=models.IntegerField(choices=[[0, 'Lunes'], [1, 'Martes'], [2, 'Miercoles'], [3, 'Jueves'], [4, 'Viernes'], [5, 'Sabado'], [6, 'Domingo']]),
        ),
    ]
