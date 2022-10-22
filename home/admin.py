from email.headerregistry import Group
from django.contrib import admin
from django.contrib.auth.models import Group

# Change header & title admin panel
admin.site.site_header = 'Rich Houses'
admin.site.site_title = 'Rich Houses'

# delete groups from admin panel
admin.site.unregister(Group)