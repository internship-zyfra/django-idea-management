from django.http import Http404
from django.views.generic import FormView, ListView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from accounts.forms import SignInForm

USER_MODEL = get_user_model()


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


class UserListView(UserPassesTestMixin, ListView):
    model = USER_MODEL

    queryset = USER_MODEL.objects.filter(is_active=True).values(
        'id', 'username', 'first_name', 'last_name', 'email', 'is_administrator', 'is_manager', 'is_author').order_by(
        'pk')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_administrator

    def handle_no_permission(self):
        raise Http404



class Page404View(TemplateView):
    template_name = 'not_found.html'
