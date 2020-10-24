from django import forms
from .models import User, Post


# ----------------------------------------------------------------
# User Forms
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',)


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password',)


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password',)


# ----------------------------------------------------------------
# Post Forms
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
