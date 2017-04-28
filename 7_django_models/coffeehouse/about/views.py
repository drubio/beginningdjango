# Create your views here.
from django.shortcuts import render
from django.http import Http404
from coffeehouse.stores.models import Store

def index(request,store_id=1):
    try:
        store = Store.objects.get(id=store_id)
        return render(request,'about/index.html',{'store':store})
    except Exception:
        raise Http404


def contact(request,store_id=1):
    try:
        store = Store.objects.get(id=store_id)
        return render(request,'about/contact.html',{'store':store})
    except Exception:
        raise Http404


