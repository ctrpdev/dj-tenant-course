from django.db import models
from django.contrib.auth.models import AbstractUser

from tenant.models import Client


class CustomUser(AbstractUser):
    tenant = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)


class FailedLoginAttempt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attempted_at = models.DateTimeField(auto_now_add=True)