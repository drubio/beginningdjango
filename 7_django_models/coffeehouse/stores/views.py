# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, JsonResponse
from coffeehouse.stores.models import Store
from coffeehouse.stores.forms import ContactCommentOnlyForm

def index(request):
    store_list = Store.objects.all()
    return render(request,'stores/index.html',  {'stores':store_list})

def detail(request,store_id=1):
    try:
        store = Store.objects.get(id=store_id)
        form = ContactCommentOnlyForm()
        vals_for_template = {'store':store,'form':form}
        return render(request,'stores/detail.html', vals_for_template)
    except Exception:
        raise Http404

def feedback(request,store_id=1):
    if request.POST:
        form = ContactCommentOnlyForm(request.POST)
        if form.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'error':form.errors})
    return HttpResponse("Hello from feedback!")
