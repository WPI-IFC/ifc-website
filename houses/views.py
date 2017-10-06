from django.shortcuts import render
from django.http import HttpResponse
from .models import Fraternity

def house_index(request):
    return render(request, "house_home.html")


def route_house(request, house):
    context = {}
    for org in Fraternity.objects.all():
        if org.lower_repr() == house:
            context["house"] = org
            break
    return render(request, "single_house.html", context)
