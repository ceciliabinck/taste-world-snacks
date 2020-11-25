from django.urls import path
from . import views

urlpatterns = [
    path('', views.box, name='box'),
    path('box_length/', views.box_length, name='box_lenght'),
]