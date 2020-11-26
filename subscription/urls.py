from django.urls import path
from . import views

urlpatterns = [
    path('', views.box, name='box'),
    path('box_length/<int:box_id>/', views.box_length, name='box_length'),
]