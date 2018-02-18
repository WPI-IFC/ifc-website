from django.shortcuts import render, get_object_or_404

from .models import BaseEvent, OfficerEvent, HouseEvent

def event_index(request):
    context = {}
    return render(request, "events_overview.html", context)


def officer_event_info(request, event_id):
    context = {"type": "officer"}
    event = get_object_or_404(OfficerEvent, id=event_id)
    context['splash'] = event.splash_img
    return render(request, "single_event.html", context)


def house_event_info(request, event_id):
    context = {"type": "house"}
    event = get_object_or_404(HouseEvent, id=event_id)
    return render(request, "single_event.html", context)
