from django.urls import path
from chain.views import CreateChainView


app_name = 'chain'

urlpatterns = [
    path('create_chain/', CreateChainView.as_view(), name='create_chain')
]
