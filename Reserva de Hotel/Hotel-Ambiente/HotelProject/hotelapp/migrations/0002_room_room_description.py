# Generated by Django 4.2.4 on 2023-08-14 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_description',
            field=models.TextField(default='Descripcion', help_text='Descripcion de la habitacion', max_length=500),
        ),
    ]