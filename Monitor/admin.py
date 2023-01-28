from django.contrib import admin
from .models import *
from .models import MonitorItem

# Register your models here.
class MonitorItemAdmin(admin.ModelAdmin):
    list_display = ('id','Name', 'Notifications')
admin.site.register(MonitorItem, MonitorItemAdmin)