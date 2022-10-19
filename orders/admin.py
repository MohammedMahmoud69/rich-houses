from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date', 'situation',)
    list_display_links = ('user', 'product',)
    list_filter = ('date', 'situation',)

admin.site.register(Order,OrderAdmin)