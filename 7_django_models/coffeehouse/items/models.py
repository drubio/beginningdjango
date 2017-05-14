# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible
class Menu(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return "%s" % (self.name)

ITEM_SIZES = (
            ('S','Small'),
            ('M','Medium'),
            ('L','Large'),
            ('P','Portion'),
            )

@python_2_unicode_compatible
class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    size = models.CharField(choices=ITEM_SIZES,max_length=1)
    calories = models.IntegerField()
    price = models.FloatField(blank=True,null=True)
    stock = models.IntegerField(default=0)
    def __str__(self):
        return "%s (%s)" % (self.name, self.description)

    
@python_2_unicode_compatible
class Drink(models.Model):
    item = models.OneToOneField(Item,on_delete=models.CASCADE,primary_key=True)
    caffeine = models.IntegerField()
    def __str__(self):
        return "%s (%s)" % (self.item, self.caffeine)
