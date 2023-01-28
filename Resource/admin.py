from django.contrib import admin
from .models import *
from .models import Resource

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CPU','Memory')

admin.site.register(Resource, ResourceAdmin)