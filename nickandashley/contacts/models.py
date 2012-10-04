from django.db import models

class Contact(models.Model):

    name             = models.CharField(max_length=255)
    email            = models.CharField(max_length=255)
    message          = models.TextField()

    created     = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.name)
