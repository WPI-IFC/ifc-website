from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.utils.timezone import now

from .models import Blog, Biography, Post
from .forms import PostForm

def officer_index(request):
    context = {}
    return render(request, "404.html", context)

def position_overview(request, slug):
    context = {}
    blog = get_object_or_404(Blog, slug=slug)
    context['perm'] = request.user.get_all_permissions()
    context['user'] = blog.current_owner
    context['biography'] = Biography.objects.get(user=blog.current_owner)
    context['position'] = blog.position_title
    context['posts'] = Post.objects.filter(blog=blog)
    return render(request, "position_overview.html", context)

@login_required
def new_post(request, slug):
    context = {}

    blog = get_object_or_404(Blog, slug=slug)
    if blog.current_owner != request.user:
        return HttpResponse(status=403) # TODO(Tom): Make this render a custom response
    
    if request.method == 'GET':
        context['form'] = PostForm()
        context['title'] = "New Post"
        return render(request, "edit_post.html", context)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.published = now()
            post.author = request.user
            post.author_string = request.user.first_name + " " + request.user.last_name
            form.save()
            return redirect('officers-view-post', slug=slug, id=post.id)

def get_post(request, slug, id):
    context = {}
    # This is how we make sure that the url is valid
    # First check that the blog exists
    blog = get_object_or_404(Blog, slug=slug)
    # Then check if the post id belongs to that blog
    context['post'] = get_object_or_404(Post, id=id, blog=blog)
    return render(request, "post.html", context)

@login_required
def edit_post(request, slug, id):
    context = {}
    # This is how we make sure that the url is valid
    # First check that the blog exists
    blog = get_object_or_404(Blog, slug=slug)
    if blog.current_owner != request.user:
        return HttpResponse(status=403) # TODO(Tom): Make this render a custom response
    # Then check if the post id belongs to that blog
    post = get_object_or_404(Post, id=id, blog=blog)
    if request.method == 'GET':
        context['form'] = PostForm(instance=post)
        context['title'] = post.title
        return render(request, "edit_post.html", context)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('officers-view-post', slug=slug, id=id)