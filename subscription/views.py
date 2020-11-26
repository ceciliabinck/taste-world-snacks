from django.shortcuts import render, get_object_or_404
from .models import Box, Length


# Create your views here.


def box(request):
    """ A view to show all boxes """

    box = Box.objects.all()

    context = {
        'box': box,
    }

    return render(request, "subscription/box.html", context)


def box_length(request, box_id):
    """ A view to show length options for box 
    so it has to get the box id from the other page"""

    length = Length.objects.all()
    box = get_object_or_404(Box, pk=box_id)
    cost = box.price
    time = length

    print(length)

    context = {
        'length': length,
        'box': box,
    }

    return render(request, "subscription/box_length.html", context)
