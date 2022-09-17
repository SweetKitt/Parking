from .models import Client, Car
from django import forms


class ClientForm(forms.ModelForm):
    GENDER_CHOISE = (('м', "мужской"),
                     ('ж', "женский"),)
    sex = forms.ChoiceField(choices=GENDER_CHOISE, label='Пол', widget=forms.Select(attrs={'class': 'form-control'}))

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


class EditCarForm(forms.ModelForm):
    is_on_parking = forms.BooleanField(label='Наличие авто на парковке', initial=True, required=False)

    class Meta:
        model = Car
        fields = ('brand', 'model', 'color', 'licence_plate', 'is_on_parking',)
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