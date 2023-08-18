from django.shortcuts import render
from .models import Reservation, Room
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_room = Room.objects.all().count()
    num_reservations = Reservation.objects.all().count()
    
    room_list = Room.objects.all()  # Assuming this is how you're querying rooms
    print(room_list)  # Add this line to print the room list # Available rooms
    num_rooms_available = Room.objects.filter(available='libre').count()

    room_types = Room.objects.values_list('room_type', flat=True).distinct()
    adults = Room.objects.values_list('room_adults', flat=True).distinct()
    childrens = Room.objects.values_list('room_childrens', flat=True).distinct()
    
    if request.method == 'POST':
        room_type = request.POST.get('room_type')
        num_adults = request.POST.get('num_adults')
        num_children = request.POST.get('num_children')

        rooms = Room.objects.filter(available='libre')

        if room_type:
            rooms = rooms.filter(room_type=room_type)
        if num_adults:
            rooms = rooms.filter(room_adults=num_adults)
        if num_children:
            rooms = rooms.filter(room_childrens=num_children)

        context = {
            'num_room': num_room,
            'num_reservations': num_reservations,
            'num_rooms_available': num_rooms_available,
            'room_list': rooms,
            'room_types': room_types,
            'adults': adults,
            'childrens': childrens,
        }
        return render(request, 'room_list.html', context)
    else:
        context = {
            'num_room': num_room,
            'num_reservations': num_reservations,
            'num_rooms_available': num_rooms_available,
            'room_list': room_list,
            'room_types': room_types,
            'adults': adults,
            'childrens': childrens,
        }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class RoomListView(generic.ListView):
    model = Room
    
class RoomDetailView(generic.DetailView):
    model = Room
