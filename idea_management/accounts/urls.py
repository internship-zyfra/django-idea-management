from django.urls import path
from accounts.views import SignInView, LogoutView, MainPageView, Page404View, UserListView

app_name = 'accounts'

urlpatterns = [
    path('login/', SignInView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('page404/', Page404View.as_view(), name='page404'),
    path("users/", UserListView.as_view(), name='users'),
    path("", MainPageView.as_view(), name='main')
]
