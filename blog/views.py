from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, redirect

from models import Blog, BlogForm


def logout_user(request):
    """Basic logout functionality."""
    logout(request)
    return redirect('blog.views.home')


def home(request):
    """Default home page - lists blogs that have been published."""
    blogs = Blog.objects.filter(Q(published__lte=datetime.now())).order_by('-published')[:10]
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context)


@login_required(login_url='/login/')
def edit(request, blog_id=None):
    """ Create a new blog entry.
    """
    if blog_id is not None:
        blog = Blog.objects.get(id=blog_id)
    else:
        blog = None
    if request.POST:
        if blog:
            form = BlogForm(request.POST, instance=blog)
        else:
            form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog.views.home')
        else:
            context = {
                'form': form
            }
            return render(request, 'blog/edit.html', context)
    if blog:
        form = BlogForm(instance=blog)
    else:
        form = BlogForm()
    context = {
        'form': form
    }
    return render(request, 'blog/edit.html', context)


@login_required(login_url='/login/')
def delete(request, blog_id):
    """ Delete a given blog.
    """
    blog = Blog.objects.get(id=blog_id)
    if blog:
        blog.delete()
    return redirect('blog.views.home')


def show_blog(request, blog_id):
    """ Show a blog detail."""
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog.html', context)