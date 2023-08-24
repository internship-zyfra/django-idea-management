from django.urls import path

from chain.views import ChainListView

app_name = 'chain'

urlpatterns = [
    path('chain_list/', ChainListView.as_view(), name='chain_list')

]