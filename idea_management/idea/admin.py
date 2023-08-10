from django.contrib import admin

from idea.models import Idea, IdeaMovement


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(IdeaMovement)
class IdeaMovementAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
