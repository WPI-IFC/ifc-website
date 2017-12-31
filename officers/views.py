from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from .models import Blog, Biography, Post

def officer_index(request):
    context = {}
    return render(request, "404.html", context)

def position_overview(request, slug):
    context = {}
    blog = get_object_or_404(Blog, slug=slug)
    context['user'] = blog.current_owner
    context['biography'] = Biography.objects.get(user=blog.current_owner)
    context['position'] = blog.position_title
    context['posts'] = Post.objects.filter(blog=blog)
    return render(request, "position_overview.html", context)