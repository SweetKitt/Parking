from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('creation', views.creation, name='creation'),
    path('creation_car', views.creation_car, name='creation_car'),
    path('editor/<int:pk>/', views.EditorView.as_view(), name='editor'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
