from django.urls import path
from accounts.views import SignInView, LogoutView

urlpatterns = [
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('logout/', LogoutView.as_view(), name='logout')
]
