from django.shortcuts import render

# Create your views here.


def countries(request):
    """ A view to return the countries page """

    return render(request, "countries/countries.html")
