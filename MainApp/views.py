from django.shortcuts import render, redirect
from .models import Post, User
from .forms import RegisterForm, LoginForm


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

def user_edit(request, pk=None):
    if pk:
        user = User.objects.filter(pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = True
            user.save()
            return redirect('user_detail', user.last_name, user.first_name)
    else:
        form = EditUserForm()
    return render(request, 'user_edit.html', {'form': form})