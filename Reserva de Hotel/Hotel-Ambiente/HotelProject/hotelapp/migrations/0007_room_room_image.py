# Generated by Django 4.2.4 on 2023-08-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0006_alter_room_available_alter_room_room_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(blank=True, null=True, upload_to='room_images/'),
        ),
    ]
