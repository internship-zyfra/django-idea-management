from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name='main'),
]