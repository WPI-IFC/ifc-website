from datetime import datetime

from django.shortcuts import render, get_object_or_404

from .models import BaseEvent, OfficerEvent, HouseEvent

def event_index(request):
    context = {}
    #TODO(Tom): Change to greater than current datetime
    context['ifc_events'] = OfficerEvent.objects.filter(d_time__lt=datetime.now()).reverse()
    context['chapter_events'] = HouseEvent.objects.filter(d_time__lt=datetime.now()).reverse()
    return render(request, "events_overview.html", context)


def officer_event_info(request, event_id):
    context = {"type": "officer"}
    event = get_object_or_404(OfficerEvent, id=event_id)
    context['title'] = event.title
    context['description'] = event.description
    context['time'] = event.d_time
    context['splash'] = event.splash_img
    return render(request, "single_event.html", context)


def chapter_event_info(request, event_id):
    context = {"type": "house"}
    event = get_object_or_404(HouseEvent, id=event_id)
    context['title'] = event.title
    context['description'] = event.description
    context['time'] = event.d_time
    context['splash'] = event.splash_img
    return render(request, "single_event.html", context)
