from django.contrib import admin

from chain.models import Chain, ChainLink, ChainLinkManager

admin.site.register(Chain, ChainLink, ChainLinkManager)
