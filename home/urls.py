from django.urls import path
from . import views
from .views import about_us, faq

# The different paths in this app


urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('faq/', faq, name='faq'),
]
