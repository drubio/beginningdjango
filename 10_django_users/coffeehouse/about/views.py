# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import ContactForm
from coffeehouse.stores.models import Store
from django.views.generic.detail import DetailView
from django.views import View

class AboutDetail(DetailView):
    model = Store
    pk_url_kwarg = 'store_id'
    template_name = 'about/index.html'
    def get_object(self):
        if 'store_id' not in self.kwargs:
            return Store.objects.get(id=1)
        else:
            return Store.objects.get(id=self.kwargs['store_id'])

class Contact(View):
    # Get handler method
    def get(self, request):
        form = ContactForm(label_suffix=' : ',initial={'user':request.user,'otherstuff':'otherstuff'},use_required_attribute=False,auto_id=False)
        return render(request,'about/contact.html',{'form':form})
        
    # Post handler method
    def post(self, request):
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # insert into DB
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/about/contact/thankyou')
        return render(request,'about/contact.html',{'form':form})
            
