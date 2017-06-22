from django.shortcuts import render
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from coffeehouse.items.models import Item, ItemForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin

class ItemList(ListView):
    model = Item
    context_object_name = 'items' # Override object_list reference for template
    template_name = 'items/index.html'

class ItemDetail(DetailView):
    model = Item
    pk_url_kwarg = 'item_id'    
    template_name = 'items/detail.html'

class ItemCreation(SuccessMessageMixin,CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s created successfully"

class ItemUpdate(SuccessMessageMixin,UpdateView):
    model = Item
    pk_url_kwarg = 'item_id'    
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s updated successfully"

class ItemDelete(DeleteView):
    model = Item
    pk_url_kwarg = 'item_id'    
    success_url = reverse_lazy('items:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Item %s removed successfully' % self.get_object().name)
        return super(ItemDelete, self).delete(request, *args, **kwargs)
