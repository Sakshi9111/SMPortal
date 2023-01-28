from django.contrib import admin
from .models import *
from .models import Item

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Created','State','Bindings', 'ServerName')



admin.site.register(Item, ItemAdmin)


# class ResourceAdmin(admin.ModelAdmin):
#     list_display = ('Name', 'CPU','Memory')

# admin.site.register(Resource, ResourceAdmin)