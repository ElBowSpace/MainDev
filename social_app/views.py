from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.shortcuts import render, redirect

from social_app.connection import connect_users
from social_app.forms import SignUpForm, NewPostForm, EditUserForm, EditPostForm
from social_app.models import Post, Connection


# ----------------------------------------------------------------
# D E F A U L T - - V I E W S
def index(request):
    return render(request, 'index.html')


def tutorial(request):
    return render(request, 'tutorial.html')


def missing(request):
    return render(request, '_missing.html')


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


# ----------------------------------------------------------------
# U S E R - - V I E W S
def user_list(request):
    all_user_list = User.objects.filter(is_active=True).order_by('last_name')
    context = {'user_list': all_user_list}
    return render(request, 'user_list.html', context)


def user_detail(request, username=None):
    if username:
        page_user = User.objects.filter(username=username)
        connected_list = get_connections_list(request.user.pk)
        if page_user and connected_list:
            if page_user[0].pk in connected_list[0].values():
                connected_list = True
            else:
                connected_list = False
        user_post_list = Post.objects.filter(user=page_user[0]).order_by('time_stamp').reverse()
        form = new_post_request(request)
        args = {'user_list': page_user, 'connections': connected_list, 'user_post_list': user_post_list, 'form': form}
        return render(request, 'user_detail.html', args)
    else:
        return missing(request)


def get_connections_list(pk=None):
    print("getting connections from table for: " + str(pk))
    queryset = Connection.objects.filter(receiver_id=pk).values('sender_id')
    sender_list = Connection.objects.filter(sender_id=pk).values('receiver_id')
    return queryset.union(queryset, sender_list)


def get_id_list(qs=None):
    list_ids = []
    for item in qs:
        list_ids.append(item['sender_id'])
    return list_ids


def make_connection(request, sender_name=None, receiver_name=None):
    sender = User.objects.get(username=sender_name)
    receiver = User.objects.get(username=receiver_name)
    connect_users(sender, receiver)
    return user_detail(request, username=receiver_name)


def user_edit(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = None
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(user.password)
            user.save()
            return redirect('user_detail', user.username)
    else:
        form = EditUserForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
    return index(request)


# ----------------------------------------------------------------
# P O S T - - V I E W S
def post_list(request, author_pk=None):
    form = new_post_request(request)
    if author_pk:
        all_post_list = Post.objects.filter(user=User.objects.get(pk=author_pk)).order_by('time_stamp').reverse()
    else:
        all_post_list = Post.objects.all().order_by('time_stamp').reverse()
    args = {'post_list': all_post_list, 'form': form}
    return render(request, 'post_list.html', args)


def post_detail(request, post_pk=None):
    form = new_post_request(request, post_pk)
    if post_pk:
        post = Post.objects.filter(pk=post_pk)
        args = {'post_list': post, 'form': form}
    else:
        args = None
    return render(request, 'post_detail.html', args)


def new_post_request(request, reply_pk=None):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.time_stamp = datetime.Now()
            post.user = request.user
            if reply_pk:
                post.reply = Post.objects.get(pk=reply_pk)
                # TODO for M-7 replies currently don't appear below post; high priority
            post.save()
    else:
        form = NewPostForm()
    return form


def post_edit(request, post_pk=None):
    if post_pk:
        post = Post.objects.get(pk=post_pk)
    else:
        post = None
    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.time_stamp = datetime.Now()
            post.save()
            return redirect('post_detail', post_pk)
    else:
        form = EditPostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def post_delete(request, pk=None):
    if pk:
        post = Post.objects.get(pk=pk)
        author = post.user
        post.delete()
        return redirect('user_detail', author.username)
    else:
        return render(request, 'post_list.html')


# TODO for M-7 user home page; Med Priority after issues
# def user_home(request):
#     return render(request, 'user_home.html')
#
