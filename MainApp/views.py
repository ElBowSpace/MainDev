from django.views.generic import TemplateView
from os.path import exists
from .models import Post


class IndexView(TemplateView):

    def get_template_names(self):
        template_name = self.kwargs.get('template', 'index.html')
        if not exists('templates/' + template_name):
            template_name = 'missing.html'
        return template_name


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
