from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from coffeehouse.items.models import Item
from django.contrib.auth.models import User
from django import forms
from django.utils.functional import lazy

class BaseItemFormSet(forms.BaseModelFormSet):
    def clean(self):
        super(BaseItemFormSet, self).clean()
        # Check errors dictionary first, if there are any error, no point in validating further
        if any(self.errors):
            return
        items = []
        for form in self.forms:
            item_id = form.cleaned_data['item']
            if item_id in items:
                raise forms.ValidationError("Ups! You have multiple %s items in your order, keep one and increase the amount" % (Item.objects.get(id=item_id)))
            items.append(item_id)

            
@python_2_unicode_compatible
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s" % (self.created)    

@python_2_unicode_compatible
class OrderItem(models.Model):
    item = models.IntegerField()
    amount = models.IntegerField()
    order = models.ForeignKey(Order)
    def __str__(self):
        return "%s" % (self.item)
    
def item_choices():
    all_items = Item.objects.all()
    menu_list = [(None,'Please select an item')]
    for item in all_items:
        menu_list.append((item.id,'%s [%s; Calories:%s; Price: %s]' % (item.name,item.description,item.calories,item.price)))    
    return menu_list


class OrderItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(OrderItemForm, self).__init__(*args, **kwargs)
       self.fields['amount'] = forms.ChoiceField(choices=[(None,'Amount of items')]+[(i, i) for i in range(1,10)],initial=0)
       self.fields['item'] = forms.ChoiceField(choices=item_choices,initial=0)
    class Meta:
        model = OrderItem
        exclude = ('order',)

