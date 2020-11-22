from django.shortcuts import render

# Create your views here.


def box(request):
    """ A view to return the choice a box page """

    return render(request, "subscription/box.html")
