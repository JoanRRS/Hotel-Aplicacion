from django.shortcuts import render, redirect
from .models import Reservation, Room
from django.views import generic 
# from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
# from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import unauthenticated_user


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
    
@login_required
def crear_reserva(request):
    if request.method == 'POST':
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        room_id = request.POST['room']
        
        # Verificar disponibilidad de la habitación
        conflicting_reservations = Reservation.objects.filter(
            room_id=room_id,
            check_in_date__lt=check_out_date,
            check_out_date__gt=check_in_date
        )

        if conflicting_reservations.exists():
            messages.warning(request, "La habitación ya está reservada en esas fechas.")
            return redirect('crear_reserva')

        
        # Crea una instancia de Reservation y guárdala en la base de datos
        reserva = Reservation(user=request.user,  # Asocia la reserva al usuario si es necesario
                              room_id=room_id,
                              check_in_date=check_in_date,
                              check_out_date=check_out_date)
        reserva.save()
        return redirect('lista')  # Redirige a la lista de reservas o a la página deseada

    return render(request, 'reserva/crear_reserva.html', {'rooms': Room.objects.all()})

@login_required
def lista_reservas(request):
    reservas = Reservation.objects.filter(user=request.user)
    return render(request, 'reserva/lista_reserva.html', {'reservas': reservas})
    
@login_required
def detalle_reserva(request, pk):
    reserva = Reservation.objects.get(pk=pk)
    check_in_date = reserva.check_in_date
    check_out_date = reserva.check_out_date

    duracion_estancia = (reserva.check_out_date - reserva.check_in_date).days


    # Calcula el número de días de la reserva
    delta = check_out_date - check_in_date
    num_dias = delta.days

    # Recupera el precio de la habitación
    precio_habitacion = reserva.room.price_per_night

    # Calcula el precio total
    precio_total = precio_habitacion * num_dias

    return render(request, 'reserva/detalle_reserva.html', {'reserva': reserva, 'precio_total': precio_total,'duracion_estancia': duracion_estancia})

@login_required
def cancelar_reserva(request, reserva_id):
    # Obtener la reserva
    reserva = Reservation.objects.get(id=reserva_id)
    
    # Calcular duración de la estancia y precio total
    check_in_date = reserva.check_in_date
    check_out_date = reserva.check_out_date
    delta = check_out_date - check_in_date
    duracion_estancia = delta.days
    precio_habitacion = reserva.room.price_per_night
    precio_total = precio_habitacion * duracion_estancia

    # Renderizar la plantilla
    context = {'reserva': reserva, 'duracion_estancia': duracion_estancia, 'precio_total': precio_total}
    if request.method == 'POST':
        try:
            reserva.delete() 
            return redirect('lista') 
        except Reservation.DoesNotExist:
            return redirect('error')
    
    return render(request, 'reserva/cancelar_reserva.html', context)


from django.shortcuts import render

def usuario(request):
    # Obtén la información del usuario, por ejemplo:
    usuario = request.user  # Suponiendo que estás utilizando la autenticación de Django

    # Ahora pasa la información del usuario al contexto
    contexto = {
        'usuario': usuario,
        # Otros datos que quieras pasar al template
    }

    return render(request, 'index.html', contexto)


@unauthenticated_user
def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.warning(request, "El nombre de usuario ya está en uso.")
            return redirect('crear_usuario')

        # Crear el usuario
        usuario = request.user 
        usuario = User.objects.create_user(username, email, password)
        usuario.save()

        messages.success(request, "Usuario creado exitosamente.")
        return redirect('login')  # Redirigir a la página de inicio de sesión

    return render(request, 'crear_usuario.html')
