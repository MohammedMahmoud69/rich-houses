from email.headerregistry import Group
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.

admin.site.site_header = 'sitescodes'
admin.site.site_title = 'sitescodes'
admin.site.unregister(Group)