from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('guestbook.views',
    (r'^post/?$', post),
)
