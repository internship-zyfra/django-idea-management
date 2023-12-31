from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class Chain(models.Model):
    chain_author_id = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class ChainLink(models.Model):
    stage_number = models.IntegerField()
    chain_link = models.ForeignKey("chain.Chain", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class ChainLinkManager(models.Model):
    manager_id = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE)
    chain_link_id = models.ForeignKey("chain.ChainLink", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
