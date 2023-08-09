from django.db import models
from django.utils import timezone

from accounts.models import User


class Chain(models.Model):
    chain_author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)


class ChainLink(models.Model):
    stage_number = models.IntegerField()
    chain_link = models.ForeignKey(Chain, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)


class ChainLinkManager(models.Model):
    manager_id = models.ForeignKey(User, on_delete=models.CASCADE)
    chain_link_id = models.ForeignKey(ChainLink, on_delete=models.CASCADE)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
