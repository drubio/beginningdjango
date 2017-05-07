# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from coffeehouse.stores.views import STORE_LIST
from django.http import Http404, HttpResponseRedirect
from .forms import ContactForm


def index(request,store_id=None):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    if store_id == None:
        store = STORE_LIST[0]
    elif store_id == "1":
        store = STORE_LIST[1]
    elif store_id == "2":
        store = STORE_LIST[2]
    elif store_id == "3":
        store = STORE_LIST[3]
    else:
        raise Http404
    return render(request,'about/index.html',{'store':store})

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
