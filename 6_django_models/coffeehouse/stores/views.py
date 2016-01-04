# Create your views here.
from django.shortcuts import render
from django.http import Http404
from coffeehouse.stores.models import Store

def index(request):
    store_list = Store.objects.all()
    return render(request,'stores/index.html',  {'stores':store_list})

def detail(request,store_id=1):
    try:
        store = Store.objects.get(id=store_id)
        vals_for_template = {'store':store}
        return render(request,'stores/detail.html', vals_for_template)
    except Exception:
        raise Http404

