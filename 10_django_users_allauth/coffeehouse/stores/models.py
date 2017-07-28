# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

from django.core.exceptions import ValidationError

class StoreQuerySet(models.QuerySet):
    def sandiego(self):
        return self.filter(city='San Diego')

    def losangeles(self):
        return self.filter(city='Los Angeles')

class StoreManager(models.Manager):
    def get_queryset(self):
        return StoreQuerySet(self.model, using=self._db)

    def sandiego(self):
        return self.get_queryset().sandiego()

    def losangeles(self):
        return self.get_queryset().losangeles()
    
class SanDiegoStoreManager(models.Manager):
    def get_queryset(self):
        return super(SanDiegoStoreManager, self).get_queryset().filter(city='San Diego')

class LosAngelesStoreManager(models.Manager):
    def get_queryset(self):
        return super(LosAngelesStoreManager, self).get_queryset().filter(city='Los Angeles')    

    
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
    objects = models.Manager()
    sandiego = SanDiegoStoreManager()
    losangeles = LosAngelesStoreManager()
    shops = StoreQuerySet.as_manager()
    def __str__(self):
        return "%s (%s,%s)" % (self.name, self.city,self.state)
    def clean(self):
        # Don't allow 'San Diego' city entries that have state different than 'CA'
        if self.city == 'San Diego' and self.state != 'CA':
            raise ValidationError('Wait San Diego is in CA!, are you sure there is another San Diego in %s ?' % (self.state))
    class Meta:
        unique_together = ("name", "email")
        default_permissions = ('add',)
        permissions = (('give_refund','Can refund customers'),('can_hire','Can hire employees'))
        
