from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.core.mail import EmailMessage
from django.template.defaultfilters import linebreaks, date

from models import *
from forms import *

def index(request):
    comments = Comment.objects.all().order_by('-created')
    return render_to_response('guestbook/index.html', locals(), context_instance=RequestContext(request))

def post(request):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #comment.save()
            msg = EmailMessage('New guestbook comment on nickandashley.org', '<strong>Name:</strong> ' + form.data['name'] + '<br><br><strong>Comment:</strong><br><br>' + form.data['comment'], 'Nick and Ashley <no-reply@nickandashley.org>', ['nick@nicksergeant.com', 'ashley@ash-taylor.com'])
            msg.content_subtype = "html"
            #msg.send()
            return HttpResponse(simplejson.dumps({'id': comment.id, 'name': comment.name, 'comment': linebreaks(comment.comment), 'created': 'On ' + date(comment.created, 'M j') + ' at ' + date(comment.created, 'g A')}), mimetype='application/json')
    return HttpResponse(simplejson.dumps({'success': False}), mimetype='application/json', status=500)
