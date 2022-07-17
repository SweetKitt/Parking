from django.db import models


class Client(models.Model):
    name_client = models.CharField('ФИО', max_length=50)
    sex_client = models.CharField('Пол(м/ж)', max_length=1)
    numbers_phone = models.CharField('Номер тел.(с 8)', max_length=11)
    address_client = models.CharField('Адрес', max_length=150)
    car_client = models.IntegerField('Кол-во авто')

    def __str__(self):
        return self.name_client

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Car(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    brand = models.CharField('Марка', max_length=50)
    model = models.CharField('Модель', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    gos_number = models.CharField('Гос номер', max_length=10)
    flag = models.BooleanField()

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


