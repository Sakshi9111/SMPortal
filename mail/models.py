from django.db import models

# Create your models here.
class Mail(models.Model):
    
    Name = models.CharField(max_length=200)
    Created = models.DateTimeField(auto_now_add=True)
    Sendmail = models.DateTimeField()
    

    def __str__(self):
        return self.Name