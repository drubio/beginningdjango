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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group

class ItemList(LoginRequiredMixin,ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'items/index.html'

class ItemDetail(UserPassesTestMixin,DetailView):
    model = Item
    pk_url_kwarg = 'item_id'    
    template_name = 'items/detail.html'
    def test_func(self):
        return self.request.user.is_authenticated
    
class ItemCreation(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s created successfully"
    permission_required = ('items.add_item',)


@method_decorator(login_required, name='dispatch')
class ItemUpdate(SuccessMessageMixin,UpdateView):
    model = Item
    pk_url_kwarg = 'item_id'    
    form_class = ItemForm
    success_url = reverse_lazy('items:index')
    success_message = "Item %(name)s updated successfully"


@method_decorator(user_passes_test(lambda u: Group.objects.get_or_create(name='Baristas') in u.groups.all()), name='dispatch')
class ItemDelete(DeleteView):
    model = Item
    pk_url_kwarg = 'item_id'    
    success_url = reverse_lazy('items:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Item %s removed successfully' % self.get_object().name)
        return super(ItemDelete, self).delete(request, *args, **kwargs)
