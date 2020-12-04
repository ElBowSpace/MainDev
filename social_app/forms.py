from django import forms
from .models import User, Post
from django.contrib.auth.forms import UserCreationForm


# ----------------------------------------------------------------
# U S E R - - F O R M S

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email', 'password',)
# TODO include this form in views.login (currently no such view exists, login is through auth users atm)


class EditUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


# ----------------------------------------------------------------
# P O S T - - F O R M S
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
