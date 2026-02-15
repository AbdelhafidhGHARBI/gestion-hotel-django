from django.shortcuts import render
from .models import Room

def room_list(request):
    """
    Affiche la liste des chambres triée par capacité croissante.
    """
    rooms = Room.objects.all().order_by('capacity')
    return render(request, 'RoomApp/room_list.html', {'rooms': rooms})
