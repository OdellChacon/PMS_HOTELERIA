# Generated by Django 4.1.7 on 2023-07-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='Promocion',
            field=models.BooleanField(default=False),
        ),
    ]
