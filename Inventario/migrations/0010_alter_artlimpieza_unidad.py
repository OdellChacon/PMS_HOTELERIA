# Generated by Django 4.1.7 on 2023-06-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0009_alter_stock_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artlimpieza',
            name='Unidad',
            field=models.IntegerField(choices=[[0, 'G'], [1, 'KG'], [2, 'MG'], [3, 'LT']]),
        ),
    ]
