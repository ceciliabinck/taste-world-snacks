from django.urls import path
from . import views
from .views import contact_us


urlpatterns = [
    path('', views.contact_us, name='contact_us'),
]