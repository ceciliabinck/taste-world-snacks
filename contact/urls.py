from django.urls import path
from . import views

# The different paths in this app


urlpatterns = [
    path('', views.contact_us, name='contact_us'),
]