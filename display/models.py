from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = 'Monitor_List'

    Choices = [('On', 'On'),
    ('Off', 'Off')]
    MonitorId=models.AutoField(primary_key=True)
    ServerName = models.CharField(max_length=50, blank=True, verbose_name="ServerName")
    Name = models.CharField(max_length=50, blank=True, verbose_name="Name")
    State = models.CharField(max_length=50, blank=True, verbose_name="State")
    Monitor = models.CharField(choices=Choices,default=Choices[1][1], max_length=20, blank=True, verbose_name="Monitor")
    Notifications = models.BooleanField(default= False, verbose_name= "Notifications")

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('index')
    