# Generated by Django 4.0.6 on 2022-08-28 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_client_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['owner'], 'verbose_name': 'Автомобиль', 'verbose_name_plural': 'Автомобили'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['name'], 'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
    ]