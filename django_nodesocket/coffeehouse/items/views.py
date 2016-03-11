from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from coffeehouse.items.models import Item

def index(request):
    item_list = Item.objects.all()
    return render(request,'items/index.html',{'items':item_list})

def detail(request,item_id):
    try:
        item = Item.objects.get(id=item_id)
        return render(request,'items/detail.html',{'item':item})
    except Exception:
        raise Http404


