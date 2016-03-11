from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.description)
    def __str__(self):
        return u"%s (%s)" % (self.name, self.description)

class Store(models.Model):
    name = models.CharField(max_length=30)    
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity,blank=True)
    def __unicode__(self):
        return u"%s (%s,%s)" % (self.name, self.city,self.state)
    def __str__(self):
        return u"%s (%s,%s)" % (self.name, self.city,self.state)

from socketIO_client import SocketIO
from urlparse import urlparse
from django.conf import settings
import json


class Special(models.Model):
    start = models.DateField()
    end = models.DateField()
    description = models.CharField(max_length=500)
    def __unicode__(self):
        return u"%s (%s,%s)" % (self.description, self.start, self.end)
    def __str__(self):
        return u"%s (%s,%s)" % (self.description, self.start, self.end)
    def save(self, *args, **kwargs):        
        # Check if the Special already exists
        if not self.pk:
            # No pk so Speical is new, push update to node.js socket
            # Parse the NODEJS_SOCKET_URL value
            parsedurl = urlparse(settings.NODEJS_SOCKET_URL)
            baseurl = "%s://%s" % (parsedurl.scheme,parsedurl.hostname)
            baseport = parsedurl.port if parsedurl.port != None else 80
            # Publish record to node.js socket
            with SocketIO(baseurl, baseport) as socketIO:
                socketIO.emit('admindailyspecials', {"special":{'description':self.description,'start':self.start.strftime("%B %d"),'end':self.end.strftime("%B %d")}})
        super(Special, self).save(*args, **kwargs)
    
