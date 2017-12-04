from django.shortcuts import render
from django.http import HttpResponse
from .models import Fraternity

def house_index(request):
    context = {}
    context['houses'] = []
    for org in Fraternity.objects.all():
        context['houses'].append((org.english_name,
        "".join(x.lower() for x in org.english_name if x != " ")))
    return render(request, "house_home.html", context)


def route_house(request, house):
    context = {}
    for org in Fraternity.objects.all():
        if org.lower_repr() == house:
            context["house"] = org
            context["has_featured_image"] = bool(org.featured_picture) # Example of django magic
                                                                       # If the field is blank, interally it is false
                                                                       # because why not
            break
    return render(request, "single_house.html", context)
