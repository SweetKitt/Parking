from django.shortcuts import render, redirect
from .models import Client, Car
from .forms import ClientForm, CarForm


def home(request):
    clients = Client.objects.all()
    return render(request, 'main/home.html', {'home': 'Все клиенты', 'clients': clients})


def creation(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('creation_car')
    else:
        form = ClientForm()
    form = ClientForm()
    return render(request, 'main/creation.html', {'form': form})


def creation_car(request):
    if request.method == 'POST':
        form2 = CarForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('home')
    else:
        form2 = CarForm()
    form2 = CarForm()
    return render(request, 'main/creationcar.html', {'form2': form2})


def editor(request):
    return render(request, 'main/editor.html')

