from __future__ import unicode_literals

from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return u"%s" % (self.name)
    def __str__(self):
        return u"%s" % (self.name)

ITEM_SIZES = (
            ('S','Small'),
            ('M','Medium'),
            ('L','Large'),
            ('P','Portion'),
            )

class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    size = models.CharField(choices=ITEM_SIZES,max_length=1)
    calories = models.IntegerField()
    price = models.FloatField(blank=True,null=True)
    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.description)
    def __str__(self):
        return u"%s (%s)" % (self.name, self.description)


class Drink(models.Model):
    item = models.OneToOneField(Item,on_delete=models.CASCADE,primary_key=True)
    caffeine = models.IntegerField()
    def __unicode__(self):
        return u"%s (%s)" % (self.item, self.caffeine)
    def __str__(self):
        return u"%s (%s)" % (self.item, self.caffeine)
