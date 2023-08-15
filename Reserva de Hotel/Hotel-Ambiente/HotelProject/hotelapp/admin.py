from django.contrib import admin

# Register your models here.

from .models import Reservation, Room

# admin.site.register(Reservation)
# admin.site.register(Room)

class ReservationInline(admin.TabularInline):
    model = Reservation

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type','room_capacity','price_per_night','available')
    list_filter = ['room_number', 'available']
    inlines=[ReservationInline]

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user','room','check_in_date','check_out_date','is_active')
    list_filter = ['check_in_date']

