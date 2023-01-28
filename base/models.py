from django.db import models
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response

# Create your models here.

class Item(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('M', 'Monitoring'),
    ]
    Name = models.CharField(max_length=200)
    Created = models.DateTimeField(auto_now_add=True)
    State = models.CharField(max_length=200, blank=True)
    Bindings = models.CharField(max_length=200, blank=True)
    ServerName = models.CharField(max_length=200, blank=True)
    # Status = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

# class MonitorItem(models.Model):
#     status_choices = [
#     ('C', 'COMPLETED'),
#     ('M', 'Monitoring'),
#     ]
#     Name = models.CharField(max_length=200)
#     Created = models.DateTimeField(auto_now_add=True)
#     State = models.CharField(max_length=200, blank=True)
#     Bindings = models.CharField(max_length=200, blank=True)
#     # ServerName = models.CharField(max_length=200, blank=True)
#     Status = models.BooleanField(default=False)
    

#     def __str__(self):
#         return self.Name

class MonitorItem(models.Model):
    status_choices = [
    ('C', 'COMPLETED'),
    ('M', 'Monitoring'),
    ]
    Name = models.CharField(max_length=200)
    
    Notifications = models.BooleanField(default=False)
    

    def __str__(self):
        return self.Name


# class Resource(models.Model):
#     Name = models.CharField(max_length=200)
#     CPU = models.IntegerField(default=0)
#     Memory = models.IntegerField(default=0)

#     def __str__(self):
#         return self.Name