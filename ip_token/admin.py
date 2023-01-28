from django.contrib import admin
from .models import *
from .models import ip_token

# Register your models here.

class ip_tokenAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'ip', 'token', 'created')
    
admin.site.register(ip_token, ip_tokenAdmin)