from django.db import models
from rest_framework.authtoken.models import Token
# Create your models here.
import uuid
import imp
import re


class ip_token(models.Model):
    server_name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(unique=True)
    token = models.CharField(max_length=100, blank=True,
                             unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.server_name
