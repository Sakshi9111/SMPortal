from django.urls import path
from .views import *
urlpatterns = [
    path('notifications', feed, name='notifications'),
    path('send-mail', SendMail, name='sendmail'),
]
