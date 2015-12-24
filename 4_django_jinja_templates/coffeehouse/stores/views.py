# Create your views here.
from django.shortcuts import render
from django.http import Http404

STORE_LIST =  [{'id':0,'name':'Corporate','address':'624 Broadway','city':'San Diego','state':'CA','email':'corporate@coffeehouse.com'},{'id':1,'name':'Downtown','address':'Horton Plaza','city':'San Diego','state':'CA','email':'downtown@coffeehouse.com'},{'id':2,'name':'Uptown','address':'1240 University Ave','city':'San Diego','state':'CA','email':'uptown@coffeehouse.com'},{'id':3,'name':'Midtown','address':'784 W Washington St','city':'San Diego','state':'CA','email':'midtown@coffeehouse.com'}]

def index(request):
    store_list = STORE_LIST[1:]
    return render(request,'stores/index.html',  {'stores':store_list})

def detail(request,store_id=1):
    if store_id == "1":
        store = STORE_LIST[1]
    elif store_id == "2":
        store = STORE_LIST[2]
    elif store_id == "3":
        store = STORE_LIST[3]
    else:
        raise Http404
    store_amenities = ['WiFi','A/C']
    store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
    vals_for_template = {'store':store,'store_amenities':store_amenities,'store_menu':store_menu}
    return render(request,'stores/detail.html', vals_for_template)

