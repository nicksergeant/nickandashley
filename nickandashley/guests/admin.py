from nickandashley.guests.models import Guest, RSVP
from django.contrib import admin

class GuestAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'category', 'sent_save_the_date', 'sent_invite', 'sent_bridal_shower_invite', 'under_21', 'notes', 'created','modified',)
    ordering = ('last_name',)
    list_filter = ('category', 'maybe', 'sent_save_the_date', 'sent_invite', 'sent_bridal_shower_invite', 'under_21', 'created',)
    search_fields = ['first_name', 'last_name']
    list_editable = ('sent_save_the_date', 'sent_invite', 'sent_bridal_shower_invite',)

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('guest_1_first_name', 'guest_1_last_name', 'attending', 'number_of_guests', 'created',)
    ordering = ('guest_1_last_name',)
    list_filter = ('attending',)
    
admin.site.register(Guest, GuestAdmin)
admin.site.register(RSVP, RSVPAdmin)
