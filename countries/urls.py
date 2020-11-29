from django.urls import path
from . import views

# The different paths in this app


urlpatterns = [
    path('', views.countries, name='countries'),
]
