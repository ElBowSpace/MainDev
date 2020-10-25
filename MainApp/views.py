from datetime import datetime
from django.shortcuts import render, redirect
from .models import Post, User
from .forms import RegisterForm, LoginForm, \
    EditUserForm, NewPostForm, EditPostForm


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = True
            user.save()
            return redirect('user_detail', user.last_name, user.first_name)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('user_list')  # valid form is filled boxes, not authorized user
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_list(request):
    all_user_list = User.objects.all()
    context = {'user_list': all_user_list}
    return render(request, 'user_list.html', context)


def user_detail(request, last_name=None, first_name=None):
    if last_name:
        user = User.objects.filter(last_name=last_name, first_name=first_name)
        args = {'user_list': user}
    else:
        args = None
    return render(request, 'user_detail.html', args)


def user_edit(request, last_name, first_name):
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


def new_post(request, author_pk=None, post_pk=None):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(pk=author_pk)
            post.time_stamp = datetime.now()
            if post_pk:
                post.reply = Post.objects.get(pk=post_pk)
            post.save()
            return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'post_new.html', {'form': form})


def post_list(request):
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
