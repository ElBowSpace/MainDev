from django.urls import path

from . import views
# see tutorial at https://tutorial.djangogirls.org/en/django_forms/
urlpatterns = [
    path('', views.index, name='index'),
    path('user/new/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('users/', views.user_list, name='user_list'),
    path('user/<last_name>_<first_name>/', views.user_detail, name='user_detail'),
    path('edit_user/<last_name>_<first_name>', views.user_edit, name='user_edit'),
]
