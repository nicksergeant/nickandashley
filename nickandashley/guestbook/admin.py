from django.contrib import admin

from models import *

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','created',)
    ordering = ('created',)

admin.site.register(Comment, CommentAdmin)