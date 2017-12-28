from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

def about(request):
    context = {'officers': [], 'errors': False}
    groups = [
        'IFC President',
        'VP Standards and Internal Operations',
        'VP Recruitment',
        'VP Communications',
        'VP Finance and Service',
        'Risk Manager',
        'Academics',
        'Activities',
        'Community Involvement',
        'Community Service',
        'Membership Development',
        'Public Relations',
        'Web',
    ]
    for group in groups:
        try:
            context['officers'].append((User.objects.filter(groups__name=group)[0], group))
        except IndexError:
            print(group)
            context['errors'] = True
    return render(request, "about.html", context)

def style(request):
    return render(request, "style-example.html")