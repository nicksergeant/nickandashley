from django.contrib import admin

from models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','created',)
    ordering = ('created',)

admin.site.register(Contact, ContactAdmin)