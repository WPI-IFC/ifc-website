from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from .models import Fraternity
from .forms import HouseForm

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
    if not "house" in context:
        raise Http404
    if request.user.groups.filter(name=context["house"].english_name).exists():
        context['has_perms'] = True        
    return render(request, "single_house.html", context)


@login_required
def house_edit(request, house):
    context = {}
    org_obj = None
    for org in Fraternity.objects.all():
        if org.lower_repr() == house:
            org_obj = org
            break
    if org_obj is None:
        raise Http404("Invalid house request: {}".format(house))

    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES, instance=org_obj)
        if form.is_valid():
            form.save() # NOTE(Tom): may want to add a timestamp feature in the future
            return redirect('house-landing', house=house)
        else:
            return render(request, "house_edit.html", {'form': form})

    elif request.method == 'GET':
        if request.user.groups.filter(name=org.english_name).exists():
            context['form'] = HouseForm(instance=org)
            context['house'] = org
            return render(request, 'house_edit.html', context)
        else:
            return HttpResponse(status=403) # TODO(Tom): Make this render a custom reponse
