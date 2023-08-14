from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import redirect
from accounts.forms import SignInForm


class SignInView(FormView):
    """Класс контроллер для логина на сайт"""

    form_class = SignInForm
    template_name = 'sign_in.html'
    success_url = 'main'

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']
        user = authenticate(self.request, email=user_email, password=password)
        if user:
            login(self.request, user)
            if not remember_me:
                self.request.session.set_expiry(0)
            return super().form_valid(form)
        return self.form_invalid(form)


class LogoutView(View):
    """Класс вьюконтроллер для logout с сайта"""

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(to='sign_in')
