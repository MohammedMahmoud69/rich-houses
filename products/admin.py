from django.contrib import admin
from .models import Product , Categories
# Register your models here.

#edit on admin panel (Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date', 'category')
    list_display_links = ['name']
    filter_fields = ('category')


admin.site.register(Product,ProductAdmin)
admin.site.register(Categories)