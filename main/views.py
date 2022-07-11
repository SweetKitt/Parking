from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm


def home(request):
    clients = Client.objects.all()
    return render(request, 'main/home.html', {'home': 'Все клиенты', 'clients': clients})


def creation(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма неверная"
    form = ClientForm()
    context = {
        'form': form
    }
    return render(request, 'main/creation.html', context)


def editor(request):
    return render(request, 'main/editor.html')

