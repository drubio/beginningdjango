# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.core.exceptions import ValidationError

from coffeehouse.stores.signals import store_closed

import logging

stdlogger = logging.getLogger(__name__)

@python_2_unicode_compatible
class Amenity(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    def __str__(self):
        return "%s (%s)" % (self.name, self.description)

@python_2_unicode_compatible
class Store(models.Model):
    name = models.CharField(max_length=30)    
    address = models.CharField(max_length=30,unique=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    email = models.EmailField()
    amenities = models.ManyToManyField(Amenity,blank=True)
    def __init__(self, *args, **kwargs):
        super(Store, self).__init__(*args, **kwargs)        
        stdlogger.info("Start __init__ Store model under stores app")        
        stdlogger.info("End __init__ Store model under stores app")
    def __str__(self):
        return "%s (%s,%s)" % (self.name, self.city,self.state)
    def clean(self):
        # Don't allow 'San Diego' city entries that have state different than 'CA'
        if self.city == 'San Diego' and self.state != 'CA':
            raise ValidationError('Wait San Diego is in CA!, are you sure there is another San Diego in %s ?' % (self.state))
    def closing(self,employee):
        stdlogger.info("Start closing() Store model, before emitting signal")
        store_closed.send(sender=self.__class__, employee=employee)
        stdlogger.info("End closing() Store model, after emitting signal")
    class Meta:
        unique_together = ("name", "email")
