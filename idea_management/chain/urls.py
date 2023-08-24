from django.urls import path
from chain.views import CreateChainView, ChainListView

app_name = 'chain'

urlpatterns = [
    path('create_chain/', CreateChainView.as_view(), name='create_chain'),
    path('chain_list/', ChainListView.as_view(), name='chain_list')
]
