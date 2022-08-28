from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('creation', views.creation, name='creation'),
    path('creation_car', views.creation_car, name='creation_car'),
    path('editor/<int:pk>/', views.EditorView.as_view(), name='editor'),
    path('editor_client/<int:pk>/', views.EditorClientView.as_view(), name='editor_client'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('delete_client/<int:id>/', views.delete_client, name='delete_client'),

]
