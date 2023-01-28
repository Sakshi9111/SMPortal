from django.contrib import admin
from .models import *
from .models import Mail 

# Register your models here.
class MailAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Created', 'Sendmail' )



admin.site.register(Mail, MailAdmin)