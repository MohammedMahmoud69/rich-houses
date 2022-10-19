from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'date')
    list_display_links = ('name' , 'email')
    filter_fields = ('date',)
    search_fields = ('name' , 'email' , 'phone_number')

    
admin.site.register(Contact,ContactAdmin)