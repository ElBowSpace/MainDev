from django.urls import path
from .views import IndexView


from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # UserListView,
    # UserDetailView,
    # UserCreateView,
    # UserUpdateView,
    # UserDeleteView,
)


urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:template>', IndexView.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/detail/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('', PostListView.as_view(), name='post_list'),
    # path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    # path('new/', UserCreateView.as_view(), name='user_new'),
    # path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    # path('', UserListView.as_view(), name='user_list'),
]
