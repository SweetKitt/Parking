from .models import Client, Car
from django import forms


class ClientForm(forms.ModelForm):
    GENDER_CHOISE = (('м', "мужской"),
                     ('ж', "женский"),)
    # name = forms.CharField(max_length=50, min_length=3, label='ФИО', widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(choices=GENDER_CHOISE, label='Пол', widget=forms.Select(attrs={'class': 'form-control'}))
    # numbers_phone = forms.CharField(max_length=11, label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # address = forms.CharField(max_length=150, label='Адрес проживания', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # car = forms.IntegerField(min_value=1, label='Кол-во авто на парковке', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ('name', 'sex', 'numbers_phone', 'address', 'cars',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'numbers_phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class CarForm(forms.ModelForm):
    owner = forms.ModelChoiceField(queryset=Client.objects.all(), label='Владелец', widget=forms.Select(attrs={'class': 'form-control'}))
    # brand = forms.CharField(label='Марка', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # model = forms.CharField(label='Модель', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # color = forms.CharField(label='Цвет', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # licence_plate = forms.CharField(label='Гос. номер', widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_on_parking = forms.BooleanField(label='Наличие авто на парковке', initial=True, required=False)

    class Meta:
        model = Car
        fields = ('owner','brand','model','color','licence_plate','is_on_parking',)
        widgets = {
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'model': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'licence_plate': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }