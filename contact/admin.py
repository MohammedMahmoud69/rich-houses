from django.contrib import admin
from .models import Contact

# Edit on contact admin panel
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'date')
    list_display_links = ('name' , 'email')
    filter_fields = ('date',)
    search_fields = ('name' , 'email' , 'phone_number')

# register contact model
admin.site.register(Contact,ContactAdmin)