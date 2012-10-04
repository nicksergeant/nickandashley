from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import EmailMessage

from models import *
from forms import *

def post(request):
    if request.POST:
        if 'human' in request.POST:
            if request.POST['human'] == '7':
                form = ContactForm(request.POST)
                if form.is_valid():
                    contact = form.save(commit=False)
                    #contact.save()
                    msg = EmailMessage('New message from nickandashley.org', '<strong>Name:</strong> ' + form.data['name'] + '<br><strong>Email:</strong> ' + form.data['email'] + '<br><br><strong>Message:</strong><br><br>' + form.data['message'], 'Nick and Ashley <no-reply@nickandashley.org>', ['nick@nicksergeant.com', 'ashley@ash-taylor.com'])
                    msg.content_subtype = "html"
                    #msg.send()
                    return HttpResponse(simplejson.dumps({'success': True}), mimetype='application/json')
    return HttpResponse(simplejson.dumps({'success': False}), mimetype='application/json', status=500)
