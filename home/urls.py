from django.contrib import admin
from django.urls import path
from . import views
from .views import how_works, about_us

urlpatterns = [
    path('', views.index, name="home"),
    path('how_works/', how_works, name="how_works"),
    path('about_us/', about_us, name="about_us"),

]
