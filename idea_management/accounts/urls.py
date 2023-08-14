from django.urls import path
from accounts.views import SignInView

urlpatterns = [
    path('sign_in/', SignInView.as_view(), name='sign_in')
]
