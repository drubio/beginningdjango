# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

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
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity,blank=True)
    def __unicode__(self):
        return u"%s (%s,%s)" % (self.name, self.city,self.state)
    def __str__(self):
        return u"%s (%s,%s)" % (self.name, self.city,self.state)
    def clean(self):
        # Don't allow 'San Diego' city entries that have state different than 'CA'
        if self.city == 'San Diego' and self.state != 'CA':
            raise ValidationError('Wait San Diego is in CA!, are you sure there is another San Diego in %s ?' % (self.state))
    class Meta:
        unique_together = ("name", "email")
