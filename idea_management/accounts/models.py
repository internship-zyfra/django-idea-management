from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        blank=True, 
        max_length=254, 
        verbose_name='email address',
        unique=True
    )
    is_administrator = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
