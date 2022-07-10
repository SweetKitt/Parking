from django.shortcuts import render
from .models import Client


def home(request):
    clients = Client.objects.all()
    return render(request, 'main/home.html', {'home': 'Все клиенты', 'clients': clients})


def creation(request):

    return render(request, 'main/creation.html')


def editor(request):
    return render(request, 'main/editor.html')

