from django.contrib import admin
from .models import Blog , Category
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'category']
    list_filter = ['date', 'category']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)