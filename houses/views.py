from django.shortcuts import render
from django.http import HttpResponse
from . import models

def house_index(request):
    return render(request, "house_home.html")


def route_house(request, house):
    return HttpResponse(house)
