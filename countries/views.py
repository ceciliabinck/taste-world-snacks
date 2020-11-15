from django.shortcuts import render
from .models import Country

# Create your views here.


def countries(request):
    """ A view to return the countries page """

    countries = Country.objects.all()

    context = {
        'countries': countries,
    }

    return render(request, "countries/countries.html", context)
