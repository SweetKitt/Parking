from django.shortcuts import render, redirect
from .models import Client, Car
from .forms import ClientForm, CarForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import UpdateView
from django.core.paginator import Paginator


def home(request):
    clients = Client.objects.all()
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/home.html', {'home': 'Все клиенты', 'clients': clients, 'cars': cars, 'page_obj': page_obj})


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
            return redirect('/')
    else:
        form2 = CarForm()
    form2 = CarForm()
    return render(request, 'main/creationcar.html', {'form2': form2})


class EditorView(UpdateView):
    model = Car
    template_name = 'main/editor.html'
    form_class = CarForm


class EditorClientView(UpdateView):
    model = Client
    template_name = 'main/editor_client.html'
    form_class = ClientForm


def delete(request, id):
    try:
        car = Car.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect("/")
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")


def delete_client(request, id):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return HttpResponseRedirect("/")
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")

