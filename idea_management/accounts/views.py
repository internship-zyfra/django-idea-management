from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView, ListView
from django.views.generic import TemplateView

from accounts.forms import SignInForm, EditUserForm

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
        return redirect('accounts:page404')


class Page404View(TemplateView):
    template_name = 'not_found.html'


class CreateUserView(FormView):
    form_class = EditUserForm
    template_name = 'user_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_administrator:
            return redirect('accounts:page404')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.is_authenticated and self.request.user.is_administrator:
            user = form.save(commit=False)
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.password = form.cleaned_data['password']
            user.is_administrator = form.cleaned_data['is_administrator']
            user.is_manager = form.cleaned_data['is_manager']
            user.is_author = form.cleaned_data['is_manager']
            user.save()
            return redirect('accounts:users')
        return redirect('accounts:page404')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
