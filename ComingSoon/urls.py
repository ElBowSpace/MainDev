from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('<str:template>', IndexView.as_view()),
]
