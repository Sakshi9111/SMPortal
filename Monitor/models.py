from django.db import models

# Create your models here.
class MonitorItem(models.Model):
    
    Name = models.CharField(max_length=200)
    
    Notifications = models.BooleanField(default=False)
    

    def __str__(self):
        return self.Name