# Generated by Django 4.1.7 on 2023-06-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0002_proveedores_stock_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='Correo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='Direccion',
            field=models.CharField(max_length=50),
        ),
    ]
