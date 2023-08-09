from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField

from accounts.models import User
from chain.models import Chain, ChainLink, ChainLinkManager


class Idea(models.Model):
    title = models.CharField(max_length=150)
    body = HTMLField()
    photo = models.ImageField(blank=True, upload_to='idea_image/')
    chain_id = models.ForeignKey(Chain, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    current_chain_link = models.ForeignKey(ChainLink, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)


class IdeaMovement(models.Model):
    IDEA_MOVEMENT_TYPE = (
        ('accept', 'Accept'),
        ('reject', 'Reject'),
    )

    type = models.CharField(choices=IDEA_MOVEMENT_TYPE, max_length=10)
    manager_id = models.ForeignKey(ChainLinkManager, blank=True, on_delete=models.CASCADE)
    is_author_reject_his_idea = models.BooleanField(default=False)
    comment = models.TextField(blank=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    current_chain_link = models.ForeignKey(ChainLink, on_delete=models.CASCADE, related_name='current_idea_movements')
    next_chain_link = models.ForeignKey(ChainLink, blank=True, on_delete=models.CASCADE,
                                        related_name='next_idea_movements')
    created_at = models.DateTimeField(default=timezone.now)
