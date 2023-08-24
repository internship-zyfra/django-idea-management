from django.views.generic import FormView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView
from chain.forms import ParentEditChainForm
from accounts.models import User
from chain.models import Chain, ChainLink, ChainLinkManager


class CreateChainView(FormView):
    form_class = ParentEditChainForm
    template_name = 'chain_edit.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_administrator:
            return redirect('accounts:page404')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.user.is_authenticated and self.request.user.is_administrator:
            try:
                chain = Chain()
                user = User.objects.get(pk=self.request.user.id)
                chain.chain_author_id = user
                chain.save()

                for stage_number in range(1, 4):
                    chain_link = ChainLink()
                    chain_link.stage_number = stage_number
                    chain_link.chain_link = chain
                    chain_link.save()
                
                query_dict = form.__dict__['data']
                for i, link_key in enumerate(query_dict, start=0):
                    if 'chain_link' in link_key:
                        chain_link_manager = ChainLinkManager()
                        chain_link_manager.manager_id = User.objects.get(pk=int(query_dict[link_key][0]))
                        id_chain = ChainLink.objects.filter(chain_link=chain).order_by('-id')[0].id
                        chain_link_manager.chain_link_id = ChainLink.objects.get(pk=id_chain)
                        chain_link_manager.save()

            except Exception as err:
                print(err)
                return redirect('chain:create_chain')
            else:
                # return redirect('chain:chain_list')
                return redirect('accounts:page404')
        form.add_error(None, 'Ошибка заполнения формы!')
        return redirect('accounts:page404')
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


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
