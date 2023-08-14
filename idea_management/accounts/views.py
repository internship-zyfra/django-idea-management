from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/main.html'
