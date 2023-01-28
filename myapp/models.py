from django.db import models

class Sites (models.Model):
    class Meta:

        verbose_name_plural = 'Sites'
    name = models.CharField(("name"), max_length=255)
    Bindings = models.CharField(("Bindings"), max_length=255)
    state = models.CharField(("state"), max_length=255)

    def __str__(self):
        return self.name