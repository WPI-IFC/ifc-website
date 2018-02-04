from django.shortcuts import render, get_object_or_404

from .models import BaseEvent, OfficerEvent, HouseEvent

def event_index(request):
    context = {}
    return render(request, "events_overview.html", context)

def event_info(request, event_id):
    context = {}
    event = get_object_or_404(BaseEvent, id=event_id)
    if type(event) is OfficerEvent:
        return redner(request, "single_event.html", context)
    elif type(event) is HouseEvent:
        return redner(request, "single_event.html", context)
