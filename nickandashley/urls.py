from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.contrib import admin

from nickandashley import settings
from nickandashley.guests.views import *

admin.autodiscover()

urlpatterns = patterns('',
    (r'^wedding-party/$', direct_to_template, {'template': 'wedding-party.html'}),
    (r'^accommodations/$', direct_to_template, {'template': 'accommodations.html'}),
    (r'^the-events/$', direct_to_template, {'template': 'the-events.html'}),
    (r'^registry/$', direct_to_template, {'template': 'registry.html'}),
    (r'^about-us/$', direct_to_template, {'template': 'about-us.html'}),
    (r'^rsvp/thanks/$', direct_to_template, {'template': 'rsvp-thanks.html'}),
    (r'^$', direct_to_template, {'template': 'home.html'}),
    (r'^guestbook/', include('nickandashley.guestbook.urls')),
    (r'^contact-us/', include('nickandashley.contacts.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^rsvp/$', rsvp),
    (r'^rsvp/total/$', rsvp_total),
    (r'^rsvp/total/csv/$', rsvp_total_csv),
)
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT.replace('\\','/')
    }),
)
