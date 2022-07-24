from django.shortcuts import render, redirect
from .models import Client, Car
from .forms import ClientForm, CarForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import UpdateView


def home(request):
    clients = Client.objects.all()
    cars = Car.objects.all()
    return render(request, 'main/home.html', {'home': 'Все клиенты', 'clients': clients, 'cars': cars})


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


class EditorView(UpdateView):
    model = Car
    template_name = 'main/editor.html'
    form_class = CarForm



def delete(request, id):
    try:
        car = Car.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect("/")
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")


