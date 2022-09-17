from django.shortcuts import render, redirect
from .models import Client, Car
from .forms import ClientForm, CarForm, EditCarForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic import UpdateView
from django.core.paginator import Paginator


def home(request):
    clients = Client.objects.all()
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        brand = request.POST.get('car')
        car = Car.objects.get(id=brand)
        car.is_on_parking = 'True'
        car.save()
    return render(request, 'main/home.html', {'home': 'Все клиенты', 'clients': clients, 'cars': cars, 'page_obj': page_obj})


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('creation_car')
        else:
            return render(request, 'main/creation.html', {'form': form})
    else:
        form = ClientForm()
    form = ClientForm()
    return render(request, 'main/creation.html', {'form': form})


def create_car(request):
    if request.method == 'POST':
        form2 = CarForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('/')
        else:
            return render(request, 'main/creationcar.html', {'form2': form2})
    else:
        form2 = CarForm()
    form2 = CarForm()
    return render(request, 'main/creationcar.html', {'form2': form2})


class EditorView(UpdateView):
    model = Car
    template_name = 'main/editor.html'
    form_class = EditCarForm

# def car_editing(request, id):
#     car = Car.objects.get(id=id)
#     if request.method == 'POST':
#         car.brand = request.POST.get('brand', car.brand)
#         car.model = request.POST.get('model', car.model)
#         car.color = request.POST.get('color', car.color)
#         car.licence_plate = request.POST.get('licence_plate', car.licence_plate)
#         car.is_on_parking = request.POST.get('is_on_parking', False)
#         car.save()
#         return HttpResponseRedirect('/')
#     else:
#         return render(request, "main/editor.html", {"car": car})


class EditorClientView(UpdateView):
    model = Client
    template_name = 'main/editor_client.html'
    form_class = ClientForm


def delete_car(request, id):
    try:
        car = Car.objects.get(id=id)
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
    car.delete()
    return HttpResponseRedirect("/")



def delete_client(request, id):
    try:
        client = Client.objects.get(id=id)
    except Car.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
    client.delete()
    return HttpResponseRedirect("/")


