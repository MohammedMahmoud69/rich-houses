from django.contrib import admin
from .models import Product , Categories

# edit product admin panel (Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'category')
    list_display_links = ['name']
    filter_fields = ('category')

# register product & category models
admin.site.register(Product,ProductAdmin)
admin.site.register(Categories)