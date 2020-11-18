from datetime import datetime
from django.shortcuts import render, redirect
from .models import Post, Connection
from .forms import EditUserForm, NewPostForm, EditPostForm
from .post import *
from .user import *
from .connection import connect_users
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def tutorial(request):
    return render(request, 'tutorial.html')


# ----------------------------------------------------------------
# User Views


def user_home(request):
    return render(request, 'user_home.html')


def user_list(request):
    all_user_list = User.objects.filter(is_active=True)
    context = {'user_list': all_user_list}
    return render(request, 'user_list.html', context)


def user_detail(request, last_name=None, first_name=None, pk=None, user_pk=None):
    args, user = None, None
    if pk:
        user = User.objects.filter(pk=pk)
    elif last_name and first_name:
        user = User.objects.filter(last_name=last_name, first_name=first_name)
    connected_list = get_connections_list(user[0].pk)
    connected_list = get_id_list(connected_list)
    if user_pk in connected_list:
        connected_list = True
    else:
        connected_list = False
    user_post_list = Post.objects.filter(user=user[0])
    print(user_post_list)
    args = {'user_list': user, 'connections': connected_list, 'user_post_list': user_post_list}
    return render(request, 'user_detail.html', args)


def get_connections_list(pk=None):
    queryset = Connection.objects.filter(receiver_id=pk).values('sender_id')
    sender_list = Connection.objects.filter(sender_id=pk).values('receiver_id')
    return queryset.union(queryset, sender_list)


def get_id_list(qs=None):
    list_ids = []
    for item in qs:
        list_ids.append(item['sender_id'])
    return list_ids


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
            user.is_active = True
            user.save()
            return redirect('user_detail', user.last_name, user.first_name)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        user.is_active = False
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
            if author_pk and post_pk:
                post.user = User.objects.get(pk=author_pk)
                post.reply = Post.objects.get(pk=post_pk)
            elif post_pk:
                post.reply = Post.objects.get(pk=post_pk)
                post.user = User.objects.get(pk=Post.objects.get(pk=post_pk).user.pk)
            elif author_pk:
                post.user = User.objects.get(pk=author_pk)
            post.time_stamp = datetime.now()
            post.save()
            return redirect('post_list')
    else:
        form = NewPostForm()
    return render(request, 'post_new.html', {'form': form})


def post_reply(request, author_pk=None, post_pk=None):
    if author_pk and post_pk:
        return redirect('new_post', author_pk=author_pk, post_pk=post_pk)


def post_list(request, viewer_pk=None, pk=None):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.time_stamp = datetime.now()
            post.user = User.objects.get(pk=viewer_pk)
            post.save()
    else:
        form = NewPostForm()
    if pk:
        all_post_list = Post.objects.filter(user=User.objects.get(pk=pk))
    else:
        all_post_list = Post.objects.all()
    args = {'post_list': all_post_list, 'form': form}
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


def make_connection(request, sender_pk=None, receiver_pk=None):
    sender = User.objects.get(pk=sender_pk)
    receiver = User.objects.get(pk=receiver_pk)
    connect_users(sender, receiver)
    return user_list(request)
