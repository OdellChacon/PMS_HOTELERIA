# Generated by Django 4.2.2 on 2023-07-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_datos_reserva_id_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservaciones',
            name='disponible',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
