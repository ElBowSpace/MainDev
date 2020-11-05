from datetime import datetime
from django.shortcuts import render, redirect
from .models import Post, User, Connection
from .forms import RegisterForm, LoginForm, \
    EditUserForm, NewPostForm, EditPostForm
from .connection import make_connection
from .post import *
from .user import *


def index(request):
    return render(request, 'index.html')


# ----------------------------------------------------------------
# User Views
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = True
            user.save()
            return redirect('user_detail', user.pk)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('user_home')  # valid form is filled boxes, not authorized user
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_home(request):
    return render(request, 'user_home.html')


def user_list(request):
    all_user_list = User.objects.filter(active=True)
    context = {'user_list': all_user_list}
    return render(request, 'user_list.html', context)


def user_detail(request, last_name=None, first_name=None, pk=None):
    args = None
    if pk:
        user = User.objects.filter(pk=pk)
        args = {'user_list': user}
    elif last_name and first_name:
        if last_name:
            user = User.objects.filter(last_name=last_name, first_name=first_name)
            args = {'user_list': user}

    return render(request, 'user_detail.html', args)


def user_edit(request, last_name, first_name, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        if last_name:
            user = User.objects.get(last_name=last_name, first_name=first_name)
        else:
            user = None
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = True
            user.save()
            return redirect('user_detail', user.last_name, user.first_name)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        user.active = False
        user.save()
        return redirect('index')
    else:
        return render(request, 'user_list.html')


# ----------------------------------------------------------------
# Post Views
def new_post(request, author_pk=None, post_pk=None):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if author_pk:
                post.user = User.objects.get(pk=author_pk)
            post.time_stamp = datetime.now()
            if post_pk:
                post.reply = Post.objects.get(pk=post_pk)
                post.user = User.objects.get(pk=Post.objects.get(pk=post_pk).user.pk)
            post.save()
            return redirect('post_list', pk=post.user.pk)
    else:
        form = NewPostForm()
    return render(request, 'post_new.html', {'form': form})


def post_reply(request, post_pk=None):
    if post_pk:
        return redirect('new_post', post_pk=post_pk)


def post_list(request, pk=None):
    if pk:
        all_post_list = Post.objects.filter(user=User.objects.get(pk=pk))
    else:
        all_post_list = Post.objects.all()
    args = {'post_list': all_post_list}
    return render(request, 'post_list.html', args)


def post_detail(request, post_pk=None):
    if post_pk:
        post = Post.objects.filter(pk=post_pk)
        args = {'post_list': post}
    else:
        args = None
    return render(request, 'post_detail.html', args)


def post_edit(request, post_pk=None):
    if post_pk:
        post = Post.objects.get(pk=post_pk)
    else:
        post = None
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.time_stamp = datetime.now()
            post.save()
            return redirect('post_detail', post_pk)
    else:
        form = EditPostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_delete(request, pk=None):
    if pk:
        post = Post.objects.get(pk=pk)
        author_id = post.user.pk
        post.delete()
        return redirect('post_list', pk=author_id)
    else:
        return render(request, 'post_list.html')


def make_connection(request, active_user=None, pk=None):
    sender = User.objects.get(pk=active_user)
    receiver = User.objects.get(pk=pk)
    make_connection(sender,receiver)
    context = {'user_list': receiver}
    return render(request, 'user_detail.html', context)
