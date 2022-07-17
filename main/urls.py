from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('creation', views.creation, name='creation'),
    path('creation_car', views.creation_car, name='creation_car'),
    path('editor', views.editor, name='editor'),
]
