from .models import Client
from django.forms import ModelForm, TextInput, Textarea


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name_client", "sex_client", "numbers_phone", "address_client",
                  "car_client"]
        widgets = {
            "name_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите ФИО"
        }),
            "sex_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите пол(м/ж)"
        }),
            "numbers_phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите номер телефона(с 8)"
        }),
            "address_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите адрес"
        }),
            "car_client": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите кол-во автомобилей"
        }),
    }