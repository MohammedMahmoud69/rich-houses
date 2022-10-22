from django.contrib import admin
from .models import Blog , Category

# Edit Blog admin panel

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'category']
    list_filter = ['date', 'category']

# register blog model
admin.site.register(Blog, BlogAdmin)
# register category model
admin.site.register(Category)