# Generated by Django 4.2.4 on 2023-08-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0007_room_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_capacity',
            field=models.IntegerField(choices=[(1, 'Adulto'), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]
