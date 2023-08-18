from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/',views.RoomListView.as_view(), name='rooms'),
    path('rooms/<int:pk>', views.RoomDetailView.as_view(), name='rooms-detail'),
    path('hotelapp/rooms/', views.index, name='roomsindex'),
]
