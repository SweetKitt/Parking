from django.db import models


class Client(models.Model):
    name_client = models.CharField('ФИО', max_length=50)
    sex_client = models.CharField('Пол(м/ж)', max_length=1)
    numbers_phone = models.CharField('Номер тел.(с 8)', max_length=11)
    address_client = models.CharField('Адрес', max_length=150)
    car_client = models.IntegerField('Кол-во авто', max_length=2)

    def __str__(self):
        return self.name_client

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'