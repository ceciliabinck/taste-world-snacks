from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, "home/index.html")


def how_works(request):
    """ A view to return the how it works section on the index page """

    return render(request, "home/index.html#works")


def about_us(request):
    """ A view to return to the about us page """

    return render(request, "home/about_us.html")
