from django.shortcuts import render
from django.contrib.auth.models import User

from officers.models import Biography, Blog, Post

def index(request):
    context = {}
    context['posts'] = Post.objects.all()[:5] # Arbitrary number of
                                              # most recent posts
    return render(request, "index.html", context)

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
            user = User.objects.filter(groups__name=group)[0]
            blog = Blog.objects.get(current_owner=user)
            context['officers'].append((user, Biography.objects.filter(user=user)[0].headshot, group, blog.slug))
        except IndexError:
            print(group)
            context['errors'] = True
    return render(request, "about.html", context)

def style(request):
    return render(request, "style-example.html")