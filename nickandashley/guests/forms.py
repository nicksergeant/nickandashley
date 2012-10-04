from django.forms import ModelForm

from guests.models import RSVP

class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
