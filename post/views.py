from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string

from post.models import Posts
from .forms import PostForm
# Create your views here.

def login_form(request, shortcode=None):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('post_list'))
        else:
            context['error'] = 'Please enter correct username and password'
            return render(request, 'post/login.html', context)
    else:
        return render(request, 'post/login.html')

#############################################################################################

def post_list(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'post/post_list.html', context)

def add_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'post/post_add.html', {'form': form})


def update_post(request, id):
    posts = Posts.objects.get(id=id)
    form = PostForm(request.POST or None, instance=posts)

    if form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'post/post_add.html', {'form': form, 'posts': posts})

def delete_post(request, id):
    posts = Posts.objects.get(id=id)

    if request.method == 'POST':
        posts.delete()
        return redirect('post_list')

    return render(request, 'post/post_delete.html', {'posts':posts})

















