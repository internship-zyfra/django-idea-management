from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from accounts.forms import SignInForm


class SignInView(FormView):
    form_class = SignInForm
    template_name = 'sign_in.html'

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        remember_me = form.cleaned_data['remember_me']
        user = authenticate(self.request, email=user_email, password=password)
        if user:
            login(self.request, user)
            if not remember_me:
                self.request.session.set_expiry(0)
            return redirect('accounts:main')
        form.add_error(None, 'Неверная почта или пароль!')
        return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('accounts:sign_in')
    

class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/main.html'
