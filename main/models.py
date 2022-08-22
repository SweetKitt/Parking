from django.db import models
from django.core.validators import MinLengthValidator


class Client(models.Model):
    GENDER_CHOISE = (('м', "мужской"),
                     ('ж', "женский"),)
    name = models.TextField('ФИО', validators=[MinLengthValidator(limit_value=3, message='Имя не может быть меньше 3х символов')])
    sex = models.CharField(max_length=1, choices=GENDER_CHOISE)
    numbers_phone = models.TextField('Номер тел.(с 8)', unique=True)
    address = models.TextField('Адрес')
    cars = models.IntegerField('Кол-во авто')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Car(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    brand = models.TextField('Марка')
    model = models.TextField('Модель')
    color = models.TextField('Цвет')
    licence_plate = models.TextField('Гос номер', unique=True)
    is_on_parking = models.BooleanField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return f'/'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


