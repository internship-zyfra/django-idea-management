from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from chain.models import Chain, ChainLink, ChainLinkManager


class ChainListView(UserPassesTestMixin, ListView):
    model = Chain
    template_name = 'chain/chain_list.html'
    context_object_name = 'chains'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_administrator

    def handle_no_permission(self):
        return redirect('accounts:page404')

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chains = context['chains']
        chain_data = []

        for chain in chains:
            managers_by_stage = {}
            chain_links = ChainLink.objects.filter(chain_link=chain, is_deleted=False)

            for link in chain_links:
                managers = ChainLinkManager.objects.filter(chain_link_id=link, is_deleted=False)
                managers_by_stage[link.stage_number] = managers

            chain_data.append({
                'chain': chain,
                'managers_by_stage': managers_by_stage,
            })

        context['chain_data'] = chain_data
        return context
