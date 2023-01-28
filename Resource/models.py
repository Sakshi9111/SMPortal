from django.db import models

# Create your models here.
class Resource(models.Model):
    Name = models.CharField(max_length=200)
    CPU = models.IntegerField(default=0)
    RAM = models.FloatField(default=0)
    Memory = models.IntegerField(default=0)

    def __str__(self):
        return self.Name