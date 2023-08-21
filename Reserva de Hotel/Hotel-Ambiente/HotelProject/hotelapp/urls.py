from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/',views.RoomListView.as_view(), name='rooms'),
    path('rooms/<int:pk>', views.RoomDetailView.as_view(), name='rooms-detail'),
    path('hotelapp/rooms/', views.index, name='roomsindex'),
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('lista/', views.lista_reservas, name='lista'),
    path('detalle_reserva/<int:pk>/', views.detalle_reserva, name='detalle_reserva'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),

]
