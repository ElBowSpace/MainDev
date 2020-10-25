from django.urls import path

from . import views
# see tutorial at https://tutorial.djangogirls.org/en/django_forms/
urlpatterns = [
    path('', views.index, name='index'),
    path('user/new/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('users/', views.user_list, name='user_list'),
    path('user/<last_name>_<first_name>/', views.user_detail, name='user_detail'),
    path('edit_user/<last_name>_<first_name>/', views.user_edit, name='user_edit'),
    path('post/new/<int:author_pk>/', views.new_post, name='new_post'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_pk>', views.post_edit, name='post_edit'),
]
