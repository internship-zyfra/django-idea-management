from django.contrib import admin

from chain.models import Chain, ChainLink, ChainLinkManager


@admin.register(Chain)
class ChainAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ChainLink)
class ChainLinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(ChainLinkManager)
class ChainLinkManagerAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
