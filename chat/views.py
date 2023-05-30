# Create your views here.
# chat/views.py
from django.shortcuts import render


def index(request):
    return render(
        request, "/home/mohamed/notifications/notification/chat/templates/index.html"
    )


def room(request, room_name):
    return render(
        request,
        "/home/mohamed/notifications/notification/chat/templates/room.html",
        {"room_name": room_name},
    )
