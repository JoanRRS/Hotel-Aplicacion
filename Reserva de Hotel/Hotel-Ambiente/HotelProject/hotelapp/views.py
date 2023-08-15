from django.shortcuts import render
from .models import Reservation, Room
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_room = Room.objects.all().count()
    num_reservations = Reservation.objects.all().count()

    # Available rooms
    num_rooms_available = Room.objects.filter(available='libre').count()


    context = {
        'num_room': num_room,
        'num_reservations': num_reservations,
        'num_rooms_available': num_rooms_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class RoomListView(generic.ListView):
    model = Room
    
class RoomDetailView(generic.DetailView):
    model = Room