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
    So now to get the"""
    # import pdb; pdb.set_trace()
    length = Length.objects.all()
    box = get_object_or_404(Box, pk=box_id)
    cost = box.price
    box_lengths = []
    for l in length:
        print(l.length)
        new_length = {'id': l.id, 'name': l.name, 'cost': l.length * cost}
        box_lengths.append(new_length)
    # month_price = cost * 2

    print(box_lengths)
    context = {
        'length': box_lengths,
        'box': box,
        'month_price': box_lengths
    }

    return render(request, "subscription/box_length.html", context)
