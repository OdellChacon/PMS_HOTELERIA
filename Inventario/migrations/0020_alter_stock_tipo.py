# Generated by Django 4.1.7 on 2023-06-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0019_stock_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Tipo',
            field=models.IntegerField(choices=[[0, 'Granos'], [1, 'Verduras'], [2, 'Frutas'], [3, 'Prod. Lacteos'], [4, 'Proteinas'], [5, 'Carne'], [6, 'Otro']]),
        ),
    ]
