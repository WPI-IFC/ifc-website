from django.shortcuts import render
from django.http import HttpResponse


def house_index(request):
    return render(request, "house_home.html")


def house_info(request, house):
    return HttpResponse(house)
