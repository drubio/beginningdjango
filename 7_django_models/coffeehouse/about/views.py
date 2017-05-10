# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .forms import ContactForm
from coffeehouse.stores.models import Store


def index(request,store_id=1):
    try:
        store = Store.objects.get(id=store_id)
        return render(request,'about/index.html',{'store':store})
    except Exception:
        raise Http404


def contact(request,store_id=None):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = ContactForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # process data, insert into DB, generate email,etc
            # redirect to a new URL:
            return HttpResponseRedirect('/about/contact/thankyou')
    else:
        # GET, generate blank form
        form = ContactForm(label_suffix=' : ',initial={'user':request.user,'otherstuff':'otherstuff'},use_required_attribute=False,auto_id=False)
    return render(request,'about/contact.html',{'form':form})
