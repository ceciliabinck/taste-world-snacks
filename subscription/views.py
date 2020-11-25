from django.shortcuts import render
from .models import Box, Length


# Create your views here.


def box(request):
    """ A view to show all boxes """

    box = Box.objects.all()

    context = {
        'box': box,
    }

    return render(request, "subscription/box.html", context)


def box_length(request):
    """ A view to show length options for box """

    length = Length.objects.all()

    context = {
        'length': length,
    }

    return render(request, "subscription/box_length.html", context)
