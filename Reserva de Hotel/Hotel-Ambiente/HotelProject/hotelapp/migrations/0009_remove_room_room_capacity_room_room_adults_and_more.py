# Generated by Django 4.2.4 on 2023-08-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0008_alter_room_room_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_capacity',
        ),
        migrations.AddField(
            model_name='room',
            name='room_adults',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
        migrations.AddField(
            model_name='room',
            name='room_childrens',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1),
        ),
    ]