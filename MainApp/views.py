from django.views.generic import TemplateView
from os.path import exists
from .models import Post


class IndexView(TemplateView):

    def get_template_names(self):
        template_name = self.kwargs.get('template', 'index.html')
        if not exists('templates/' + template_name):
            template_name = 'missing.html'
        return template_name

# Post Class views------------------------------------------------------------------- 

class PostListView(TemplateView):
    model = Post
    template_name = 'post_list.html'


class PostDetailView(TemplateView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(TemplateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class PostUpdateView(TemplateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class PostDeleteView(TemplateView):
    model = Post
    template_name = 'post_delete.html'
    # success_url = reverse_lazy('post_list')

# User Class views-------------------------------------------------------------------
# # Im thinking of these these as being viewed by admin not by the user.
# class UserListView(TemplateView):
#     model = User
#     template_name = 'user_list.html'  


# class UserDetailView(TemplateView):
#     model = User
#     template_name = 'user_detail.html'


# class UserCreateView(TemplateView):
#     model = User
#     template_name = 'user_new.html'
#     fields = ['first_name', 'last_name', 'email', 'password']


# class UserUpdateView(TemplateView):
#     model = User
#     template_name = 'user_edit.html'
#     fields = ['first_name', 'last_name', 'email']


# class UserDeleteView(TemplateView):
#     model = User
#     template_name = 'user_delete.html'
#     # success_url = reverse_lazy('User_list')