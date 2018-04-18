from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from .models import BaseEvent, OfficerEvent, HouseEvent
from .forms import OfficerEventForm, HouseEventForm

def event_index(request):
    context = {}
    #TODO(Tom): Change to greater than current datetime
    context['ifc_events'] = OfficerEvent.objects.filter(d_time__gt=datetime.now()).reverse()
    context['chapter_events'] = HouseEvent.objects.filter(d_time__gt=datetime.now()).reverse()
    return render(request, "events_overview.html", context)


@login_required
@permission_required('events.add_officerevent', raise_exception=True)
def new_officer_event(request):
    context = {}

    if request.method == 'GET':
        context['form'] = OfficerEventForm()
        context['title'] = "New Event"
        return render(request, "edit_event.html", context)
    elif request.method == 'POST':
        form = OfficerEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            form.save()
            return redirect("event-officer-overview", id=event.id)


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
