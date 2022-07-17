from .models import Client, Car
from django import forms


class ClientForm(forms.ModelForm):
    GENDER_CHOISE = (('м', "мужской"),
                     ('ж', "женский"), )
    name_client = forms.CharField(max_length=50, min_length=3, label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex_client = forms.ChoiceField(choices=GENDER_CHOISE, label='Пол', widget=forms.Select(attrs={'class': 'form-control'}))
    numbers_phone = forms.CharField(max_length=11, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_client = forms.CharField(max_length=150, label='Адрес проживания', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    car_client = forms.IntegerField(min_value=1, label='Кол-во авто на парковке', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ('name_client', 'sex_client', 'numbers_phone', 'address_client', 'car_client',)


class CarForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Client.objects.all(), label='Владелец', widget=forms.Select(attrs={'class': 'form-control'}))
    brand = forms.CharField(max_length=50, label='Марка', widget=forms.TextInput(attrs={'class': 'form-control'}))
    model = forms.CharField(max_length=50, label='Модель', widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.CharField(max_length=50, label='Цвет', widget=forms.TextInput(attrs={'class': 'form-control'}))
    gos_number = forms.CharField(max_length=10, label='Гос. номер', widget=forms.TextInput(attrs={'class': 'form-control'}))
    flag = forms.BooleanField(label='Наличие авто на парковке', initial=True)

    class Meta:
        model = Car
        fields = ('owner','brand','model','color','gos_number','flag',)