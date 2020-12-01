from django.conf.urls import url
from django.urls import path, include
from social_app import views

# see tutorial at https://tutorial.djangogirls.org/en/django_forms/
urlpatterns = [
    path('', views.index, name='index'),
    path('user_guide/', views.tutorial, name='tutorial'),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    path('accounts/signup/', views.signup, name='signup'),
    path('users/', views.user_list, name='user_list'),
    path('user/<str:username>/', views.user_detail, name='user_detail'),
    path('edit_user/<int:pk>/', views.user_edit, name='user_edit'),
    path('delete_user/<int:pk>', views.user_delete, name='user_delete'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_pk>', views.post_edit, name='post_edit'),
    path('delete_post/<int:pk>/', views.post_delete, name='post_delete'),
    path('missing/', views.missing, name='missing'),
    path('connection/new/<str:sender_name>/<str:receiver_name>', views.make_connection, name='make_connection'),
]
