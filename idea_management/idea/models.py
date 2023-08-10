from django.contrib.auth import get_user_model
from django.db import models

from sorl.thumbnail import ImageField
from tinymce.models import HTMLField


class Idea(models.Model):
    title = models.CharField(max_length=150)
    body = HTMLField()
    photo = ImageField(blank=True, null=True, upload_to='idea_image/')
    chain_id = models.ForeignKey("chain.Chain", on_delete=models.CASCADE)
    author_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    current_chain_link = models.ForeignKey("chain.ChainLink", null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class IdeaMovement(models.Model):
    ACCEPT = 1
    REJECT = 2
    IDEA_MOVEMENT_TYPE = (
        (ACCEPT, 'Accept'),
        (REJECT, 'Reject'),
    )

    type = models.PositiveSmallIntegerField(choices=IDEA_MOVEMENT_TYPE)
    manager_id = models.ForeignKey("chain.ChainLinkManager", null=True, blank=True, on_delete=models.CASCADE)
    is_author_reject_his_idea = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    idea = models.ForeignKey("idea.Idea", on_delete=models.CASCADE)
    current_chain_link = models.ForeignKey("chain.ChainLink", on_delete=models.CASCADE,
                                           related_name='current_idea_movements')
    next_chain_link = models.ForeignKey("chain.ChainLink", null=True, blank=True, on_delete=models.CASCADE,
                                        related_name='next_idea_movements')

    created_at = models.DateTimeField(auto_now=True)
