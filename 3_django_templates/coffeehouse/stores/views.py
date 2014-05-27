# Create your views here.
from django.shortcuts import render

def index(request):
    store_list = [{"id":1,"name":'Downtown'},{"id":2,"name":'Uptown'},{"id":3,"name":'Midtown'}]
    return render(request,'stores/index.html',  {'stores':store_list})


def detail(request,store_id=1):
    if store_id == "1":
        STORE_NAME = 'Downtown'
        store_address = {'street':'385 Main','city':'San Diego','state':'CA'}
    elif store_id == "2":
        STORE_NAME = 'Uptown'
        store_address = {'street':'231 Highland','city':'San Diego','state':'CA'}
    else:
        STORE_NAME = 'Midtown'
        store_address = {'street':'85 Balboa','city':'San Diego','state':'CA'}
    store_amenities = ['WiFi','A/C']
    store_menu = ((0,''),(1,'Drinks'),(2,'Food'))
    vals_for_template = {'store_name':STORE_NAME,'store_address':store_address,'store_amenities':store_amenities,'store_menu':store_menu}
    return render(request,'stores/detail.html', vals_for_template)    
