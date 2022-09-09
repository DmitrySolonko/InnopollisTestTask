from django.contrib import admin
from .models import Item


# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']
    list_display_links = ['id', 'name', 'description', 'price']


admin.site.register(Item, ItemAdmin)
