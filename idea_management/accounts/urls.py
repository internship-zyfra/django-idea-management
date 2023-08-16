from django.urls import path
from accounts.views import SignInView, LogoutView, MainPageView, UserListView

app_name = 'accounts'

urlpatterns = [
    path('login/', SignInView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("", MainPageView.as_view(), name='main'),
    path("users/", UserListView.as_view(), name='users')
]
