from django.contrib import admin
from .models import Order

# Edit on order admin panel
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'date', 'situation',)
    list_display_links = ('user', 'product',)
    list_filter = ('date', 'situation',)

# register order model
admin.site.register(Order,OrderAdmin)