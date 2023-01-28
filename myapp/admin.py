from django.contrib import admin
from .models import *
from .models import Sites


class SitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'Bindings')

admin.site.register(Sites, SitesAdmin)
