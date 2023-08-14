from django.db import models
from django.urls import reverse

# Create your models here.
from django.contrib.auth.models import User
import datetime

class Room(models.Model):
    """Model representing a hotel room."""
    ROOM_TYPES = (
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    )

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default='Single')
    room_description = models.TextField(max_length=500, help_text="Descripcion de la habitacion",default='Descripcion')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        """String for representing the Model object."""
        return f"Room {self.room_number} - {self.room_type}"
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this room."""
        return reverse('rooms-detail', args=[str(self.id)])

class Reservation(models.Model):
    """Model representing a room reservation."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """String for representing the Model object."""
        return f"Reservation for {self.user.username} - Room {self.room.room_number}"

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this reservation."""
        return reverse('reservation-detail', args=[str(self.id)])
